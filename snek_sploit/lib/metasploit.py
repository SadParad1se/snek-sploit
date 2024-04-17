import urllib3
from typing import Union

from snek_sploit.lib.context import Context, RPCResponse
from snek_sploit.lib.rpc.auth import Auth
from snek_sploit.lib.rpc.consoles import Consoles
from snek_sploit.lib.rpc.core import Core
from snek_sploit.lib.rpc.db import DB
from snek_sploit.lib.rpc.health import Health
from snek_sploit.lib.rpc.jobs import Jobs
from snek_sploit.lib.rpc.modules import Modules
from snek_sploit.lib.rpc.plugins import Plugins
from snek_sploit.lib.rpc.sessions import Sessions


class MetasploitClient:
    def __init__(
        self,
        username: str,
        password: str,
        host: str = "127.0.0.1",
        port: int = 55553,
        uri: str = "/api/",
        ssl: bool = True,
        certificate: str = "",
        log_in: bool = True,
        token: str = "",
        disable_https_warnings: bool = False,
        timeout: Union[float, tuple] = None,
        verbose: bool = False,
    ):
        """
        Client used for communication with MSF RPC.
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

        self._context = Context(username, password, host, port, uri, ssl, certificate, token, timeout, verbose)

        self.auth = Auth(self._context)
        self.consoles = Consoles(self._context)
        self.core = Core(self._context)
        self.db = DB(self._context)
        self.health = Health(self._context)
        self.jobs = Jobs(self._context)
        self.modules = Modules(self._context)
        self.plugins = Plugins(self._context)
        self.sessions = Sessions(self._context)

        if log_in:
            self.login()

    def login(self) -> None:
        """
        Login.
        :return: None
        """
        self.auth.login()

    def logout(self) -> None:
        """
        Logout.
        :return: None
        """
        self.auth.rpc.logout(self._context.token)

    def call(self, endpoint: str, arguments: list = None, **kwargs) -> RPCResponse:
        """
        Wrapper for `self.context.call`.
        :param endpoint: Endpoint name
        :param arguments: Arguments that will be processed and passed to the endpoint
        :param kwargs: use_token, timeout
        :return: Raw RPC response
        """
        return self._context.call(endpoint, arguments, **kwargs)
