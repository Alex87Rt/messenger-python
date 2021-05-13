import os
import inspect
import binascii

from functools import wraps

DEFAULT_SERVER_PORT = 8006
TCP_MSG_BUFFER_SIZE = 1024
DEFAULT_SERVER_IP = '127.0.0.1'
CLIENTS_COUNT_LIMIT = 20
SERVER_LOGGER_NAME = 'messenger.server'
CLIENT_LOGGER_NAME = 'messenger.client'
DEFAULT_CLIENT_LOGIN = 'User'
DEFAULT_CLIENT_PASSWORD = 'Password'


def get_this_script_full_dir():
    return os.path.dirname(os.path.realpath(__file__))


def log_func_call(logger):
    def log_func_call_decorator(func):
        @wraps(func)
        def log_func_call_decorated(*args, **kwargs):
            ret = func(*args, **kwargs)
            logger.info(f'Called function {func.__name__} '
                        f'with parameters: {args} {kwargs}, '
                        f'returned: {ret}, '
                        f'caller name: {str(inspect.stack()[1][3])}')
            return ret

        return log_func_call_decorated

    return log_func_call_decorator


class Menu:
    def __init__(self, commands: list):
        self._commands = {i + 1: item for i, item in enumerate(commands)}

    def get_command(self, command_index):
        return self._commands[command_index]

    def __str__(self):
        result = '\nChoose command:\n'
        for key, val in self._commands.items():
            result += f'{key}. {val}\n'
        result += '>'
        return result


def bytes_to_hexstring(data: bytes) -> str:
    return binascii.hexlify(data).decode('utf-8')


def hexstring_to_bytes(hexstring: str) -> bytes:
    return binascii.unhexlify(hexstring)
