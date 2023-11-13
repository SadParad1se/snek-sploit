from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCCore(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Core.html
    """
    VERSION = "core.version"
    STOP = "core.stop"
    GETG = "core.getg"
    SETG = "core.setg"
    UNSETG = "core.unsetg"
    SAVE = "core.save"
    RELOAD_MODULES = "core.reload_modules"
    ADD_MODULE_PATH = "core.add_module_path"
    MODULE_STATS = "core.module_stats"
    THREAD_LIST = "core.thread_list"
    THREAD_KILL = "core.thread_kill"
