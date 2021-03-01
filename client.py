# Программа сервера для отправки приветствия сервера и получения ответа
from socket import *
import json

with socket(AF_INET, SOCK_STREAM) as s:  # Создать сокет TCP
    s.connect(("localhost", 8007))  # Соединиться с сервером

    with open('client_config.json') as f:
        message_json = json.load(f)

    message = json.dumps(message_json)
    s.send(message.encode("utf-8"))
    data = s.recv(1000000)
    str = data.decode("utf-8")
    print("Сообщение от сервера: ", str, ", длиной ", len(data), " байт")

    recv_msg = json.loads(str)

    print(f"Сообщение {recv_msg}")
