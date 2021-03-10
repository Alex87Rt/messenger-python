# Программа сервера для получения приветствия от клиента и отправки ответа
from contextlib import closing
from socket import *
import json

with socket(AF_INET, SOCK_STREAM) as s:  # Создает сокет TCP
    s.bind(("", 8007))  # Присваивает порт 8007
    s.listen()

    while True:
        client, addr = s.accept()
        with closing(client) as cl:
            data = cl.recv(1000000)
            str = data.decode("utf-8")
            print("Сообщение: ", str, ", было отправлено клиентом:", addr)
            recv_msg = json.loads(str)

            if "action" in recv_msg and recv_msg['action'] == 'authenticate':
                with open('json/server_config.json') as f:
                    message = json.load(f)
                message = json.dumps(message)
                cl.send(message.encode("utf-8"))
