from socket import *
import client_def
from contextlib import closing

from log.client_log_config import *

host = '127.0.0.1'
port = 8006

with socket(AF_INET, SOCK_STREAM) as s:
    client_data_to_send = client_def.client_data_encode()
    s.connect((host, port))
    s.send(client_data_to_send)
    with closing(s):
        data = s.recv(10000)
        message = client_def.server_resp_to_str(data)
        print(message)
        client_logger.debug(message)