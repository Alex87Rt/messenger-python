import argparse
import sys
import select
import helpers
import logging
import inspect
import log_config
import os
from time import sleep

from socket import *
from jim import request_from_bytes, JimResponse
from storage import DBStorageServer

log = logging.getLogger(helpers.SERVER_LOGGER_NAME)


def parse_commandline_args(cmd_args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='listen_address', type=str, default='')
    parser.add_argument('-p', dest='listen_port', type=int, default=helpers.DEFAULT_SERVER_PORT)
    return parser.parse_args(cmd_args)


class ServerVerifier(type):
    def __init__(cls, clsname, bases, clsdict):
        tcp_found = False

        for key, value in clsdict.items():
            if not hasattr(value, '__call__'):
                continue

            source = inspect.getsource(value)
            if '.connect(' in source:
                raise RuntimeError('Сервер не должен использовать соединение для сокетов')

            if 'SOCK_STREAM' in source:
                tcp_found = True

        if not tcp_found:
            raise RuntimeError('Сервер должен использовать только сокеты TCP')

        type.__init__(cls, clsname, bases, clsdict)


class Server(metaclass=ServerVerifier):
    def __init__(self, storage):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__storage = DBStorageServer(storage)

    def set_settings(self, listen_address, listen_port,
                     clients_limit=helpers.CLIENTS_COUNT_LIMIT, timeout=helpers.SERVER_SOCKET_TIMEOUT):
        self.__socket.bind((listen_address, listen_port))
        self.__socket.listen(clients_limit)
        self.__socket.settimeout(timeout)

    def __del__(self):
        self.__socket.close()

    @property
    def storage(self):
        return self.__storage

    def mainloop(self):
        clients = []
        logins = {}


        while True:
            try:
                conn, addr = self.__socket.accept()
            except OSError:
                pass
            else:
                print(f'Клиент подключен: {str(addr)}')
                clients.append(conn)
            finally:
                readable, writable, erroneous = [], [], []
                try:
                    readable, writable, erroneous = select.select(clients, clients, clients, 0)
                except:
                    pass

                for client_socket in readable:
                    try:
                        if client_socket not in writable:
                            continue
                        request = request_from_bytes(client_socket.recv(helpers.TCP_MSG_BUFFER_SIZE))
                        responses = []
                        if request.action == 'presence':
                            client_login = request.datadict['user']['account_name']
                            client_time = request.datadict['time']
                            client_ip = client_socket.getpeername()[0]
                            resp = JimResponse()
                            if client_login not in logins.values():
                                logins[client_socket] = client_login
                                server.storage.update_client(client_login, client_time, client_ip)
                                resp.response = 200
                            elif client_socket in logins.keys() and logins[client_socket] == client_login:
                                server.storage.update_client(client_login, client_time, client_ip)
                                resp.response = 200
                            else:
                                resp.response = 400
                                resp.set_field('ошибка', 'Клиент находится в сети')
                            responses.append(resp)
                            print(resp)
                        elif request.action == 'add_contact':
                            client_login = logins[client_socket]
                            contact_login = request.datadict['user_id']
                            resp = JimResponse()
                            if not server.storage.check_client_exists(contact_login):
                                resp.response = 400
                                resp.set_field('ошибка', f'Такого клиента нет: {contact_login}')
                            elif server.storage.check_client_in_contacts(client_login, contact_login):
                                resp.response = 400
                                resp.set_field('ошибка', f'Клиент уже нахоидтся в контактах: {contact_login}')
                            else:
                                server.storage.add_client_to_contacts(client_login, contact_login)
                                resp.response = 200
                            responses.append(resp)
                            print(resp)
                        elif request.action == 'del_contact':
                            client_login = logins[client_socket]
                            contact_login = request.datadict['user_id']
                            resp = JimResponse()
                            if not server.storage.check_client_exists(contact_login):
                                resp.response = 400
                                resp.set_field('ошибка', f'Такого клиента нет: {contact_login}')
                            elif not server.storage.check_client_in_contacts(client_login, contact_login):
                                resp.response = 400
                                resp.set_field('ошибка', f'Клиент уже нахоидтся в контактах: {contact_login}')
                            else:
                                server.storage.del_client_from_contacts(client_login, contact_login)
                                resp.response = 200
                            responses.append(resp)
                            print(resp)
                        elif request.action == 'get_contacts':
                            client_login = logins[client_socket]
                            client_contacts = server.storage.get_client_contacts(client_login)
                            quantity_resp = JimResponse()
                            quantity_resp.response = 202
                            quantity_resp.set_field('quantity', len(client_contacts))
                            responses.append(quantity_resp)
                            print(quantity_resp)
                            for contact in client_contacts:
                                contact_resp = JimResponse()
                                contact_resp.set_field('action', 'contact_list')
                                contact_resp.set_field('user_id', contact)
                                responses.append(contact_resp)
                                print(contact_resp)
                        elif request.action == 'msg':
                            resp = JimResponse()
                            resp.response = 200
                            responses.append(resp)

                            print(resp)
                        else:
                            raise RuntimeError(f'Ошибка с JIM {request.action}')
                        for resp in responses:
                            sleep(0.01)
                            client_socket.send(resp.to_bytes())
                    except BaseException as e:
                        print(f'Клиент отключен: {client_socket.getpeername()}, {e}')
                        client_socket.close()
                        clients.remove(client_socket)
                        try:
                            del logins[client_socket]
                        except:
                            pass
                        if client_socket in writable:
                            writable.remove(client_socket)


if __name__ == '__main__':
    print('Сервер запущен')
    log.info('Сервер запущен')
    try:
        args = parse_commandline_args(sys.argv[1:])
        server = Server(os.path.join(helpers.get_this_script_full_dir(), 'server.sqlite'))
        server.set_settings(args.listen_address, args.listen_port)
        server.mainloop()
    except Exception as e:
        log.critical(str(e))
        raise e
