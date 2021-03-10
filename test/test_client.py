from unittest.mock import MagicMock

from Client.client import Client
from Client.messages import Authenticate


def test_authenticate():

    mock_sock = MagicMock()
    mock_serializer = MagicMock()
    sut = Client(mock_sock, "username", mock_serializer)

    mock_serializer.serialize.return_value = b"123TEST"

    sut.authenticate("password")

    # assert mock_serializer.msg == Authenticate("username", "password")
    mock_serializer.serialize.assert_called_once_with(
        Authenticate("username", "password")
    )
    # assert mock_sock.sent_data == b"123TEST"
    mock_sock.send.assert_called_once_with(b"123TEST")


def test_mock_example():
    mock_fn = MagicMock()
    mock_fn("a", 1, b"3")
    mock_fn.assert_called_once_with("a", 1, b"3")
