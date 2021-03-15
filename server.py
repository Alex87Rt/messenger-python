from socket import *
from contextlib import closing
import server_def

from log.server_log_config import *
host = ''
port = 8006
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    while True:
        client, addr = s.accept()
        with closing(client):
            data = client.recv(1000000)
            print(f"Сообщение: {str(client)}, было отправлено клиентом: {addr} ")
            data_cl = data.decode('utf-8')
            message = server_def.server_resp(server_def.client_data(data_cl))
            message_json = str(message).encode('utf-8')
            client.send(message_json)
            server_logger.debug(message)