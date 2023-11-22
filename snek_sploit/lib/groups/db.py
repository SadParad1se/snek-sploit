from snek_sploit.lib.base import Base, Context
from snek_sploit.lib.rpc import RPCDB


class DB(Base):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCDB(context)
