from snek_sploit.lib.base import Base, Context
from snek_sploit.lib.rpc import RPCAuth


class Auth(Base):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCAuth(context)

    def login(self):
        token = self.rpc.login(self._context.username, self._context.password)
        self._context.token = token
        self.rpc.token_add(token)
