import urllib3

from snek_sploit.lib.context import Context
from snek_sploit.lib.auth import Auth


class Client:
    def __init__(self, username: str, password: str, host: str = "127.0.0.1", port: int = 55553, uri: str = "/api/",
                 ssl: bool = True, certificate: str = "", log_in: bool = True, token: str = "",
                 disable_https_warnings: bool = False):
        if disable_https_warnings:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.context = Context(username, password, host, port, uri, ssl, certificate, token)
        self.auth = Auth(self.context)

        if log_in:
            self.login()

    def login(self):
        token = self.auth.login(self.context.username, self.context.password)
        self.context.token = token
        self.auth.token_add(token)

    def logout(self):
        self.auth.logout(self.context.token)

    def call(self, endpoint: str, arguments: list = None) -> dict:
        return self.context.call(endpoint, arguments)
