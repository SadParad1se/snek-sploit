from enum import StrEnum


class ModuleType(StrEnum):  # TODO: str enum is supported since 3.11
    """
    List of the existing module types.
    """
    exploit = "exploit"
    auxiliary = "auxiliary"
    post = "post"
    nop = "nop"
    payload = "payload"


class SessionType(StrEnum):  # TODO: str enum is supported since 3.11
    """
    List of the existing session types.
    """
    shell = "shell"
    meterpreter = "meterpreter"
    ring = "ring"
