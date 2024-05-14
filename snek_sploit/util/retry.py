from functools import wraps, partial


def retry(func=None, *, tries: int = 1, on_errors: tuple = None):
    """
    Retry a function if an error occurs.
    :param func: Original function
    :param tries: Number of times to retry
    :param on_errors: On what errors to retry
    :return: Wrapper
    """
    if func is None:
        return partial(retry, tries=tries, on_errors=on_errors)

    if not on_errors:
        on_errors = (Exception,)

    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(tries + 1):
            try:
                return func(*args, **kwargs)
            except on_errors as ex:
                if i == tries:
                    raise ex

    return wrapper
