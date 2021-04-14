import os
import inspect
from functools import wraps

DEFAULT_SERVER_PORT = 8007
TCP_MSG_BUFFER_SIZE = 1024
CLIENTS_COUNT_LIMIT = 25
DEFAULT_SERVER_IP = '127.0.0.1'
SERVER_SOCKET_TIMEOUT = 0.3
SERVER_LOGGER_NAME = f'messenger.server'
CLIENT_LOGGER_NAME = f'messenger.client'
DEFAULT_CLIENT_LOGIN = 'UserTest'


def get_this_script_full_dir():
    return os.path.dirname(os.path.realpath(__file__))


def log_func_call(logger):
    def log_func_call_decorator(func):
        @wraps(func)
        def log_func_call_decorated(*args, **kwargs):
            ret = func(*args, **kwargs)
            logger.info(
                f'Вызываемая функция {func.__name__} с параметрами: {args} {kwargs}, возвращает: {ret}, имя вызывающего абонента: {str(inspect.stack()[1][3])}')
            return ret

        return log_func_call_decorated

    return log_func_call_decorator
