import time
import json


CLIENT_REQUEST = {"action": "authenticate",
                  "time": '<unix timestamp>',

                   "user": { "account_name": "C0deMaver1ck",

                            "password":     "CorrectHorseBatterStaple" }
                  }



SERVER_RESPONSE = {
    "response": '<код ответа>',
    "alert": '<текст ответа>'
                   }



SERVER_RESPONSE_200 = {
    "response": 200,
    "alert":"Необязательное сообщение/уведомление"
}


SERVER_RESPONSE_402 = {
    "response": 402,
    "error": "This could be wrong password or no account with that name"
}


SERVER_RESPONSE_409 = {
    "response": 409,
    "error": "Someone is already connected with the given user name"
}

SERVER_QUIT = {
    "action": "quit"
}

def data_clients_input():

    account_name = input("Send your account name: ")
    action = "presence"
    data_time = time.time()
    data_type = "online"
    data_client_json = {"action": action,
        "time": data_time,
        "type": data_type,
        "user": {
                "account_name":  account_name,
                "status":      "Yep, I am here!"}}
    data_clients_presence = json.dumps(data_client_json, ensure_ascii=False)

    return data_clients_presence



CLIENT_PRESENS = {
        "action": "presence",
        "time": "<unix timestamp>",
        "type": "status",
        "user": {
                "account_name":  "алекс",
                "status":      "Yep, I am here!"
        }
}

SERVER_PROBE = {
        "action": "probe",
        "time": '<unix timestamp>',
}
SERVER_RESPONSE_ALERT = {
    "response": '1xx / 2xx',
    "time": '<unix timestamp>',
    "alert": "message (optional for 2xx codes)"
}

SERVER_RESPONSE_ERROR = {
    "response": '4xx / 5xx',
    "time": '<unix timestamp>',
    "error": "error message (optional)"
}

CLIENT_TO_CLIENT = {
    "action": "msg",
    "time": '<unix timestamp>',
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}




