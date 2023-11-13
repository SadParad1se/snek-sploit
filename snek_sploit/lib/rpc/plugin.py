from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCPlugin(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Plugin.html
    """
    LOAD = "plugin.load"
    UNLOAD = "plugin.unload"
    LOADED = "plugin.loaded"
