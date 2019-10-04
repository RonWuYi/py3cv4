import time
from functools import wraps

def timethis(func):
    '''
    Decorate that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        while True:
            end = time.time()
            if end - start >= 5.0:
                break
            else:
                # result = func(*args, **kwargs)
                func(*args, **kwargs)
                print(func.__name__, end-start)
    return wrapper