from snek_sploit.lib.base import Base
from snek_sploit.util import api


class Auth(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Auth.html
    """
    def login(self, username, password):
        response = self.context.call(api.AUTH_LOGIN, [username, password])

        if response[b"result"] == b"success":
            return response[b"token"].decode()

        raise Exception("Unable to login")

    def logout(self):
        response = self.context.call(api.AUTH_LOGOUT)

        if response[b"result"] == b"success":
            return

        raise Exception("Unable to logout")

    def token_list(self):
        response = self.context.call(api.AUTH_TOKEN_LIST)

        if response[b"result"] == b"success":
            return

        raise Exception("Unable to logout")

    def token_add(self, token):
        response = self.context.call(api.AUTH_TOKEN_ADD, [token])

        if response[b"result"] == b"success":
            return

        raise Exception("Unable to logout")

    def token_generate(self):
        response = self.context.call(api.AUTH_TOKEN_GENERATE)

        if response[b"result"] == b"success":
            return

        raise Exception("Unable to logout")

    def token_remove(self):
        response = self.context.call(api.AUTH_TOKEN_REMOVE)

        if response[b"result"] == b"success":
            return

        raise Exception("Unable to logout")