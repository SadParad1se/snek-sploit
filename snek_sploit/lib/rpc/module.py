from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCModule(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Module.html
    """
    EXPLOITS = "module.exploits"
    EVASION = "module.evasion"
    AUXILIARY = "module.auxiliary"
    PAYLOADS = "module.payloads"
    ENCODERS = "module.encoders"
    NOPS = "module.nops"
    POST = "module.post"
    INFO_HTML = "module.info_html"
    INFO = "module.info"
    SEARCH = "module.search"  # TODO: does this work?
    COMPATIBLE_PAYLOADS = "module.compatible_payloads"
    COMPATIBLE_EVASION_PAYLOADS = "module.compatible_evasion_payloads"
    COMPATIBLE_SESSIONS = "module.compatible_sessions"
    TARGET_COMPATIBLE_PAYLOADS = "module.target_compatible_payloads"
    TARGET_COMPATIBLE_EVASION_PAYLOADS = "module.target_compatible_evasion_payloads"
    RUNNING_STATS = "module.running_stats"
    OPTIONS = "module.options"
    EXECUTE = "module.execute"
    CHECK = "module.check"
    RESULTS = "module.results"
    EXECUTABLE_FORMATS = "module.executable_formats"
    TRANSFORM_FORMATS = "module.transform_formats"
    ENCRYPTION_FORMATS = "module.encryption_formats"
    PLATFORMS = "module.platforms"
    ARCHITECTURES = "module.architectures"
    ENCODE_FORMATS = "module.encode_formats"
    ENCODE = "module.encode"
