import json

from Client.messages import Authenticate
from Client.serializer import Serializer


def test_serialize_authenticate():
    msg = Authenticate("C0deMaver1ck", "CorrectHorseBatterStaple")

    expected_time = 256
    expected_msg = {
        "action": "authenticate",
        "time": expected_time,
        "user": {"account_name": msg.account_name, "password": msg.password,},
    }
    expected_data = json.dumps(expected_msg).encode("utf-8")

    sut = Serializer(get_time_fn=lambda: expected_time)
    assert sut.serialize(msg) == expected_data
