from Client.client_socket import ClientSocket


def test_init():
    sock = object()
    sut = ClientSocket(sock)
    assert sut._s == sock
