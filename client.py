
from socket import *
from Client.client import Client


def main(HOST, PORT):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        client_socket = Client(s)
        print(client_socket)


if __name__ == "__main__":
    main("localhost", 8007)
