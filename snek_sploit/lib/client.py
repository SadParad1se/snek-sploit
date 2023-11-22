import urllib3
from typing import Union

from snek_sploit.lib.context import Context, RPCResponse
from snek_sploit.lib.groups import Auth, Console, Core, DB, Health, Job, Module, Plugin, Session


class Client:
    def __init__(self, username: str, password: str, host: str = "127.0.0.1", port: int = 55553, uri: str = "/api/",
                 ssl: bool = True, certificate: str = "", log_in: bool = True, token: str = "",
                 disable_https_warnings: bool = False, timeout: Union[float, tuple] = None, verbose: bool = False):
        """
        Client is used for communication with MSF RPC.
        :param username: Username used for authentication
        :param password: Password used for authentication
        :param host: MSF RPC Host
        :param port: MSF RPC Port
        :param uri: API uri
        :param ssl: Whether the server is using SSL(TLS) or not
        :param certificate: Path to the certificate used for SSL(TLS)
        :param log_in: Whether to automatically login
        :param token: Token used for authentication
        :param disable_https_warnings: Whether to disable warnings for an untrusted certificate
        :param timeout: Timeout for the RPC
        :param verbose: Whether to print the raw RPC response
        """
        if disable_https_warnings:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.context = Context(username, password, host, port, uri, ssl, certificate, token)
        self.auth = Auth(self.context)
        self.console = Console(self.context)
        self.core = Core(self.context)
        self.db = DB(self.context)
        self.health = Health(self.context)
        self.job = Job(self.context)
        self.module = Module(self.context)
        self.plugin = Plugin(self.context)
        self.session = Session(self.context)

        if log_in:
            self.login()

    def login(self) -> None:
        """
        Wrapper for login.
        :return: None
        """
        self.auth.login()

    def logout(self) -> None:
        """
        Wrapper for logout.
        :return: None
        """
        self.auth.rpc.logout(self.context.token)

    def call(self, endpoint: str, arguments: list = None, **kwargs) -> RPCResponse:
        """
        Wrapper for `self.context.call`.
        :param endpoint: Endpoint name
        :param arguments: Arguments that will be processed and passed to the endpoint
        :param kwargs: use_token, timeout
        :return: Raw RPC response
        """
        return self.context.call(endpoint, arguments, **kwargs)
