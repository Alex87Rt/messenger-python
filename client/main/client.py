import sys
import os
import argparse
import logging
import inspect

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue
from client.main import helpers
from client.main import jim
from client.main.storage import DBStorageClient
from client.main import security

log = logging.getLogger(helpers.CLIENT_LOGGER_NAME)


def parse_commandline_args(cmd_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-sa', dest='server_ip', type=str,
                        default=helpers.DEFAULT_SERVER_IP)
    parser.add_argument('-sp', dest='server_port', type=int,
                        default=helpers.DEFAULT_SERVER_PORT)
    parser.add_argument('-u', dest='user_name', type=str,
                        default=helpers.DEFAULT_CLIENT_LOGIN)
    parser.add_argument('-p', dest='user_password', type=str,
                        default=helpers.DEFAULT_CLIENT_PASSWORD)
    return parser.parse_args(cmd_args)


class ClientVerifier(type):
    def __init__(cls, clsname, bases, clsdict):
        tcp_found = False

        for key, value in clsdict.items():
            if type(value) is socket:
                raise RuntimeError

            if not hasattr(value, '__call__'):
                continue

            source = inspect.getsource(value)
            if '.accept(' in source or '.listen(' in source:
                raise RuntimeError

            if 'SOCK_STREAM' in source:
                tcp_found = True

        if not tcp_found:
            raise RuntimeError('Клиент должен использовать только сокеты TCP')

        type.__init__(cls, clsname, bases, clsdict)


class Client(metaclass=ClientVerifier):
    def __init__(self, username, password, storage_file):
        self.__username = username
        self.__security_key = security.create_password_hash(password)
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__storage = DBStorageClient(storage_file)
        self.__service_messages = Queue()
        self.__user_messages = Queue()
        self.__reader_thread = Thread(target=self.read_message_thread_function)
        self.__reader_thread.daemon = True
        self.__need_terminate = False

    def __del__(self):
        self.close_client()

    def close_client(self):
        self.__socket.close()
        self.__need_terminate = True
        self.__reader_thread.join()

    def read_message_thread_function(self):
        while True:
            if self.__need_terminate:
                return
            try:
                msg = self.receive_message_from_server()
                if 'action' in msg.datadict.keys() \
                        and msg.datadict['action'] == 'msg':
                    self.__user_messages.put(msg)
                else:
                    self.__service_messages.put(msg)
            except OSError:
                pass

    @property
    def user_messages_queue(self):
        return self.__user_messages

    @property
    def username(self):
        return self.__username

    @property
    def storage(self):
        return self.__storage

    def send_data(self, data: bytes) -> int:
        if type(data) is not bytes:
            raise TypeError
        return self.__socket.send(data)

    def receive_data(self, size=helpers.TCP_MSG_BUFFER_SIZE) -> bytes:
        if size <= 0:
            raise ValueError
        return self.__socket.recv(size)

    def send_message_to_server(self, msg: jim.JimRequest):
        msg_bytes = msg.to_bytes()
        msg_bytes_len = len(msg_bytes)
        bytes_sent = self.send_data(msg_bytes)
        if bytes_sent != msg_bytes_len:
            raise RuntimeError(f'socket.send() returned {bytes_sent}, '
                               f'but expected {msg_bytes_len}')

    def receive_message_from_server(self) -> jim.JimResponse:
        received_data = self.receive_data()
        return jim.response_from_bytes(received_data)

    def check_connection(self):
        request = jim.presence_request(self.__username)
        self.send_message_to_server(request)
        response = self.__service_messages.get()
        if response.response == 200:
            return
        elif response.response == 401:
            self.authenticate(response.datadict['token'])
        else:
            raise RuntimeError(f'Presence: expected 200, '
                               f'received {response.response}, '
                               f'error: {response.datadict["error"]}')

    def authenticate(self, auth_token: str):
        auth_dig = security.create_auth_digest(self.__security_key, auth_token)
        auth_message = jim.auth_client_message(self.__username, auth_dig)
        self.send_message_to_server(auth_message)
        response = self.__service_messages.get()
        if response.response != 200:
            raise RuntimeError(f'Authenticate: expected 200, '
                               f'received {response.response}, '
                               f'error: {response.datadict["error"]}')

    def connect(self, server_ip: str, server_port: int):
        self.__socket.connect((server_ip, server_port))
        self.__reader_thread.start()
        self.check_connection()

    def update_contacts_from_server(self):
        request = jim.get_contacts_request()
        self.send_message_to_server(request)
        response = self.__service_messages.get()
        if response.response != 202:
            raise RuntimeError(f'Get contacts: expected 202, '
                               f'received: {response.response}, '
                               f'error: {response.datadict["error"]}')
        contacts_server = []
        for _ in range(0, response.datadict['quantity']):
            contact_message = self.__service_messages.get()

            if contact_message.datadict['action'] != 'contact_list':
                raise RuntimeError(f'Get contacts: '
                                   f'expected action "contact_list", '
                                   f'received: '
                                   f'{contact_message.datadict["action"]}')
            if contact_message.datadict['user_id'] not in contacts_server:
                contacts_server.append(contact_message.datadict['user_id'])

        self.storage.update_contacts(contacts_server)

    def add_contact_on_server(self, login: str):
        if not login:
            raise RuntimeError('Login cannot be empty')
        request = jim.add_contact_request(login)
        self.send_message_to_server(request)
        response = self.__service_messages.get()
        if response.response != 200:
            raise RuntimeError(f'Add contact: expected response 200, '
                               f'received: {response.response}, '
                               f'error: {response.datadict["error"]}')

    def delete_contact_on_server(self, login: str):
        if not login:
            raise RuntimeError('Login cannot be empty')
        request = jim.delete_contact_request(login)
        self.send_message_to_server(request)
        response = self.__service_messages.get()
        if response.response != 200:
            raise RuntimeError(f'Delete contact: expected response 200, '
                               f'received: {response.response}, '
                               f'error: {response.datadict["error"]}')

    def get_current_contacts(self) -> list:
        contacts = self.storage.get_contacts()
        return contacts if contacts else []

    def send_message_to_contact(self, login: str, message: str):
        if not message:
            raise RuntimeError('Message cannot be empty')
        request = jim.message_request(self.username, login, message)
        self.send_message_to_server(request)
        response = self.__service_messages.get()
        if response.response != 200:
            raise RuntimeError(f'Send message: expected response 200, '
                               f'received: {response.response}, '
                               f'error: {response.datadict["error"]}')
        self.storage.add_message(login, message)

    def get_messages(self, login: str) -> list:
        messages = self.storage.get_messages(login)
        return [{'text': item[0],
                 'incoming': bool(item[1])} for item in messages]


def check_new_inc_message_thread_function(message_queue: Queue):
    while True:
        if message_queue:
            msg = message_queue.get()
            formatted_message = f"Новое сообщение от " \
                                f"{msg.datadict['from']}: " \
                                f"{msg.datadict['message']}"
            print(formatted_message)


if __name__ == '__main__':
    try:
        args = parse_commandline_args(sys.argv[1:])
        storage_file = os.path.join(helpers.get_this_script_full_dir(),
                                    f'{args.user_name}.sqlite')
        client = Client(username=args.user_name,
                        password=args.user_password,
                        storage_file=storage_file)
        print(f'Запущенный клиент с именем пользователя {client.username}')
        print(f'Подключение к серверу {args.server_ip} '
              f'с портом {args.server_port}...')
        client.connect(args.server_ip, args.server_port)
        print('Подключено, обновление контактов...')
        client.update_contacts_from_server()
        print('Запуск монитора входящих сообщений...')
        incoming_monitor = Thread(target=check_new_inc_message_thread_function,
                                  args=(client.user_messages_queue,))
        incoming_monitor.daemon = True
        incoming_monitor.start()

        supported_commands = ['show_contacts',
                              'add_contact',
                              'delete_contact',
                              'send_message']
        main_menu = helpers.Menu(supported_commands)
        while True:
            user_choice = None
            try:
                user_choice = int(input(main_menu))
                command = main_menu.get_command(user_choice)
                if command == 'show_contacts':
                    client.update_contacts_from_server()
                    print(client.get_current_contacts())
                elif command == 'add_contact':
                    client.add_contact_on_server(input('Напечатать '
                                                       'логин '
                                                       'добавляемого '
                                                       'пользователя: >'))
                elif command == 'delete_contact':
                    client.delete_contact_on_server(input('Напечатать '
                                                          'логин '
                                                          'пользователя, '
                                                          'которого '
                                                          'нужно '
                                                          'удалить: >'))
                elif command == 'send_message':
                    current_contacts = client.get_current_contacts()
                    if not current_contacts:
                        print('Нет доступных контактов')
                        continue
                    login_to = input('Напечатать логин пользователя: >')
                    text = input('Набрать текст: >')
                    client.send_message_to_contact(login_to, text)
            except KeyboardInterrupt:
                exit(1)
            except BaseException as e:
                print(f'Ошибка: {str(e)}')
                continue
    except BaseException as e:
        log.critical(str(e))
        raise e
