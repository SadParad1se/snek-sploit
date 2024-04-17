from enum import Enum


class ModuleType(str, Enum):  # StrEnum is supported since 3.11
    """
    List of the existing module types.
    """

    EXPLOIT = "exploit"
    AUXILIARY = "auxiliary"
    POST = "post"
    NOP = "nop"
    PAYLOAD = "payload"


class SessionType(str, Enum):  # StrEnum is supported since 3.11
    """
    List of the existing session types.
    """

    SHELL = "shell"
    METERPRETER = "meterpreter"
    RING = "ring"
