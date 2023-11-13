from snek_sploit.lib.base import Base
from snek_sploit.util import api, constants


class RPCAuth(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Auth.html
    """
    def login(self, username: str, password: str) -> str:
        """
        Authenticate the client using the provided credentials.
        :param username: Username
        :param password: Password
        :return: Token used for the login
        :full response example: {b'result': b'success', b'token': b'TEMPYggAMQ7ju8z93UzZCrN6Ecx7BHWW'}
        """
        response = self._context.call(api.AUTH_LOGIN, [username, password])

        return response[constants.TOKEN].decode()

    def logout(self, token: str) -> bool:
        """
        Logout and remove (temporary) token.
        :param token: Token used by the client
        :return: True in case the logout was successful
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(api.AUTH_LOGOUT, [token])

        return response[constants.RESULT] == constants.SUCCESS

    def token_list(self) -> list[str]:
        """
        List existing tokens.
        :return: List of the existing tokens
        :full response example: {b'tokens': [b'TEMPd3GhuK6Nc0YCeS38oBpT0ZIG6VZs']}
        """
        response = self._context.call(api.AUTH_TOKEN_LIST)

        return response[constants.TOKENS]

    def token_add(self, token: str) -> bool:
        """
        Add a token into the database.
        :param token: Token to add
        :return: True in case the token was added
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(api.AUTH_TOKEN_ADD, [token])

        return response[constants.RESULT] == constants.SUCCESS

    def token_generate(self) -> str:
        """
        Generate a new token and save it to the Database.
        :return: New token
        :full response example: {b'result': b'success', b'token': b'TEMP6120290898789284108532566914'}
        """
        response = self._context.call(api.AUTH_TOKEN_GENERATE)

        return response[constants.TOKEN]

    def token_remove(self, token: str) -> bool:
        """
        Remove an existing token.
        :param token: Token to remove
        :return: True in case the removal was successful
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(api.AUTH_TOKEN_REMOVE, [token])

        return response[constants.RESULT] == constants.SUCCESS
