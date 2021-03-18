import inspect2

from functools import wraps
from log.client_log_config import *


def log(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        stack = inspect2.stack()
        logger.debug(f"Function {fn.__name__} was called from {stack[1].function}")
        return fn(*args, **kwargs)

    return inner()


@log
def foo():
    pass


@log
def bar():
    foo()


bar()
