from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCHealth(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Health.html
    """
    CHECK = "health.check"
