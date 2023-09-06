import time
from functools import wraps


def timetracked(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tic = time.time()
        result = func(*args, **kwargs)
        tac = time.time()
        print(f"Execution time ({func.__name__}): {tac-tic}")
        return result
    return wrapper
