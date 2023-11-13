from snek_sploit.lib.base import Base, Context
from snek_sploit.lib.rpc import RPCModule


class Module(Base):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCModule(context)
