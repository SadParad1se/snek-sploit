from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.lib.rpc import RPCConsoles, ConsoleInfo


class Consoles(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCConsoles(context)
