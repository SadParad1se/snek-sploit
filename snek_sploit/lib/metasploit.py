from typing import Union

from snek_sploit.lib.client import Client
from snek_sploit.lib.groups import Auth, Consoles, Core, DB, Health, Jobs, Modules, Plugins, Sessions


class Metasploit:
    def __init__(self, username: str, password: str, host: str = "127.0.0.1", port: int = 55553, uri: str = "/api/",
                 ssl: bool = True, certificate: str = "", log_in: bool = True, token: str = "",
                 disable_https_warnings: bool = False, timeout: Union[float, tuple] = None, verbose: bool = False):
        """
        Wrapper for an MSF RPC client.
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
        self.client = Client(
            username, password, host, port, uri, ssl, certificate, log_in, token, disable_https_warnings, timeout,
            verbose
        )

        self.auth = Auth(self.client)
        self.consoles = Consoles(self.client)
        self.core = Core(self.client)
        self.db = DB(self.client)
        self.health = Health(self.client)
        self.jobs = Jobs(self.client)
        self.modules = Modules(self.client)
        self.plugins = Plugins(self.client)
        self.sessions = Sessions(self.client)
