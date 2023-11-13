from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCJob(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Job.html
    """
    LIST = "job.list"
    STOP = "job.stop"
    INFO = "job.info"
