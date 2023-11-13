from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCSession(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Session.html
    """
    LIST = "session.list"
    STOP = "session.stop"
    SHELL_READ = "session.shell_read"
    SHELL_WRITE = "session.shell_write"
    SHELL_UPGRADE = "session.shell_upgrade"
    METERPRETER_READ = "session.meterpreter_read"
    METERPRETER_WRITE = "session.meterpreter_write"
    METERPRETER_SESSION_DETACH = "session.meterpreter_session_detach"
    METERPRETER_SESSION_KILL = "session.meterpreter_session_kill"
    METERPRETER_TABS = "session.meterpreter_tabs"
    METERPRETER_RUN_SINGLE = "session.meterpreter_run_single"
    METERPRETER_SCRIPT = "session.meterpreter_script"
    METERPRETER_TRANSPORT_CHANGE = "session.meterpreter_transport_change"
    METERPRETER_DIRECTORY_SEPARATOR = "session.meterpreter_directory_separator"
    COMPATIBLE_MODULES = "session.compatible_modules"
    RING_READ = "session.ring_read"
    RING_PUT = "session.ring_put"
    RING_LAST = "session.ring_last"
    RING_CLEAR = "session.ring_clear"
