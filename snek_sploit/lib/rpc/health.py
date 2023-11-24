from snek_sploit.lib.context import ContextBase
from snek_sploit.util import constants


class RPCHealth(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Health.html
    """
    CHECK = "health.check"

    def check(self) -> bool:
        """
        Check if the service is currently healthy and ready to accept requests.
        :return: True in case of success
        :full response example: {'status': b'UP'}
        """
        response = self._context.call(self.CHECK, use_token=False)

        return response[constants.STATUS] == constants.B_UP
