from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.lib.rpc import RPCCore


class Core(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCCore(context)
