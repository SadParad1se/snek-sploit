from snek_sploit.lib.base import Base, Context
from snek_sploit.lib.rpc import RPCPlugin


class Plugin(Base):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCPlugin(context)
