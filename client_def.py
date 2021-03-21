import json
import time


def data_clients_input():
    data_time = time.time()
    CLIENT_TO_CLIENT = {"action": "msg",
                        "time": data_time,
                        "to": "account_name",
                        "from": "account_name",
                        "encoding": "ascii",
                        "message": "message"
                        }
    data_clients = json.dumps(CLIENT_TO_CLIENT, ensure_ascii=False)
    return data_clients


def client_data_encode():
    data_client = data_clients_input()
    data_to_send = data_client.encode('utf-8')
    return data_to_send


def server_resp_to_str(a):
    server_resp = json.dumps(a.decode('utf-8'), ensure_ascii=False, sort_keys=True)
    return server_resp
