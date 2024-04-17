from typing import List

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants


class RPCAuth(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Auth.html
    """

    LOGIN = "auth.login"
    LOGOUT = "auth.logout"
    TOKEN_ADD = "auth.token_add"
    TOKEN_REMOVE = "auth.token_remove"
    TOKEN_LIST = "auth.token_list"
    TOKEN_GENERATE = "auth.token_generate"

    def login(self, username: str, password: str) -> str:
        """
        Authenticate the client using the provided credentials.
        :param username: Username
        :param password: Password
        :return: Token used for the login
        :full response example: {b'result': b'success', b'token': b'TEMPYggAMQ7ju8z93UzZCrN6Ecx7BHWW'}
        """
        response = self._context.call(self.LOGIN, [username, password], use_token=False)

        return response[constants.B_TOKEN].decode()

    def logout(self, token: str) -> bool:
        """
        Logout and remove (temporary) token.
        :param token: Token used by the client
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.LOGOUT, [token])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def token_add(self, token: str) -> bool:
        """
        Add a token into the database.
        :param token: Token to add
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.TOKEN_ADD, [token])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def token_remove(self, token: str) -> bool:
        """
        Remove an existing token.
        :param token: Token to remove
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.TOKEN_REMOVE, [token])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def token_list(self) -> List[str]:
        """
        List existing tokens.
        :return: List of the existing tokens
        :full response example: {b'tokens': [b'TEMPd3GhuK6Nc0YCeS38oBpT0ZIG6VZs']}
        """
        response = self._context.call(self.TOKEN_LIST)

        return [token.decode() for token in response[constants.B_TOKENS]]

    def token_generate(self) -> str:
        """
        Generate a new token and save it to the Database.
        :return: New token
        :full response example: {b'result': b'success', b'token': b'TEMP6120290898789284108532566914'}
        """
        response = self._context.call(self.TOKEN_GENERATE)

        return response[constants.B_TOKEN].decode()


class Auth(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCAuth(context)

    def login(self):
        token = self.rpc.login(self._context.username, self._context.password)
        self._context.token = token
        self.rpc.token_add(token)
