from functools import wraps, partial
import time


def retry(func=None, *, attempts: int = 1, on_errors: tuple = None, wait_on_error: bool = True):
    """
    Retry a function if an error occurs.
    :param func: Original function
    :param attempts: Number of times to retry
    :param on_errors: On what errors to retry
    :param wait_on_error: Whether to wait when an error occurs or not
    :return: Wrapper
    """
    if func is None:
        return partial(retry, attempts=attempts, on_errors=on_errors, wait_on_error=wait_on_error)

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
                if wait_on_error:
                    time.sleep(min(i + 1 * 3, 30))

    return wrapper
