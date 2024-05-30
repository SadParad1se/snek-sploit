from functools import wraps, partial
import time


def retry(func=None, *, attempts: int = 1, on_errors: tuple = None):
    """
    Retry a function if an error occurs.
    :param func: Original function
    :param attempts: Number of times to retry
    :param on_errors: On what errors to retry
    :return: Wrapper
    """
    if func is None:
        return partial(retry, attempts=attempts, on_errors=on_errors)

    if not on_errors:
        on_errors = (Exception,)

    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except on_errors as ex:
                if i + 1 == attempts:
                    raise ex
                time.sleep(min(i + 1 * 2, 30))

    return wrapper
