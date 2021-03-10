import socket
import json

from Client.serializer import Serializer

class ClientSocket:
    def __init__(self, socket):
        self._socket = socket

    def send(self, send):
        self._socket = send

    def recv(self, recv):
        self._socket = recv