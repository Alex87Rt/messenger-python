import json
import unittest


def test_data_clients_input():
    data_time = 123
    data_client_json = {"action": "authenticate",
                        "time": data_time,
                        "user": {
                            "account_name": "C0deMaver1ck",
                            "password": "CorrectHorseBatteryStaple"}}
    data_clients = json.dumps(data_client_json, ensure_ascii=False)
    assert data_clients
