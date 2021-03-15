import json
import time

SERVER_RESPONSE_200 = {
    "response": 200,
    "alert": "Необязательное сообщение/уведомление"
}

SERVER_RESPONSE_ERROR = {
    "response": '4xx / 5xx',
    "time": '<unix timestamp>',
    "error": "error message (optional)"
}


def client_data(a):
    data_client = a
    objs = json.loads(data_client)
    client_resp = dict()
    for section, commands in objs.items():
        client_resp[section] = commands
    return client_resp


def server_resp_200(account_name, account_password):
    server_answer = {
        "response": 200,
        "alert": f"Привет {account_name}!, Ваш пароль {account_password}. Время запроса: {time.time()}"
    }
    print(server_answer)
    return server_answer


def server_resp(client_resp):
    if client_resp['action'] == 'authenticate':
        account_name = client_resp['user']['account_name']
        account_password = client_resp['user']['password']
        answer = server_resp_200(account_name, account_password)
        return answer
    else:
        return SERVER_RESPONSE_ERROR
