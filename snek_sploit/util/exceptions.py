class Error(Exception):
    """
    Base Error class for Metasploit client.
    """


class RPCError(Error):
    """
    Exception raised in case the response is an error.
    """


class InputError(Error):
    """
    Exception raised in case the input is incorrect.
    """
