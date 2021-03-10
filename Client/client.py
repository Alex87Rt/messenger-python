from Client.messages import Authenticate


class Client:
    def __init__(self, client_socket, account_name, serializer):
        self._client_socket = client_socket
        self._account_name = account_name
        self._serializer = serializer

    def authenticate(self, password):
        msg = Authenticate(self._account_name, password)
        data = self._serializer.serialize(msg)
        self._client_socket.send(data)
