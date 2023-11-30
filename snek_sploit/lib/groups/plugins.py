from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.lib.rpc import RPCPlugin


class Plugins(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCPlugin(context)
