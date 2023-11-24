from abc import ABC, abstractmethod

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.lib.rpc import RPCSession, SessionInformation


class BaseSession(ABC):
    def __init__(self, rpc: RPCSession, session_id: int):
        self.rpc = rpc
        self.id = session_id
        try:
            self.info = self.fetch_information()
        except Exception:
            raise Exception(f"Unable to fetch information about the session with id {self.id}. Make sure it exists.")

    def fetch_information(self) -> SessionInformation:
        return self.rpc.list_sessions()[self.id]

    @abstractmethod
    def write(self, data: str) -> bool:
        pass

    @abstractmethod
    def read(self) -> str:
        pass


class ShellSession(BaseSession):
    def write(self, data: str) -> bool:
        pass

    def read(self) -> str:
        pass


class MeterpreterSession(BaseSession):
    pass


class RingSession(BaseSession):
    pass


class Session(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCSession(context)
