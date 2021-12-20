"""Measure the execution time of the function received as an argument"""

import time
from functools import wraps


def stopwatch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__}:{elapsed_time}秒")
        return result

    return wrapper
