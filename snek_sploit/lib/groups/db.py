from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.lib.rpc import RPCDB


class DB(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCDB(context)
