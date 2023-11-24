from abc import ABC, abstractmethod
from typing import List, Union, Dict

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.lib.rpc import RPCSession, SessionInformation, MeterpreterSessionTransportOptions
from snek_sploit.util import SessionType


class BaseSession(ABC):
    def __init__(self, rpc: RPCSession, session_id: int):
        self._rpc = rpc
        self.id = session_id
        try:
            self.info = self.fetch_information()
        except Exception:
            raise Exception(f"Unable to fetch information about the session with id {self.id}. Make sure it exists.")

    def fetch_information(self) -> SessionInformation:
        return self._rpc.list_sessions()[self.id]

    def kill(self) -> bool:
        return self._rpc.stop(self.id)

    def compatible_post_modules(self):
        return self._rpc.compatible_modules(self.id)

    @abstractmethod
    def write(self, data: str) -> bool:
        pass

    @abstractmethod
    def read(self) -> str:
        pass


class ShellSession(BaseSession):
    def write(self, data: str) -> bool:
        self._rpc.shell_write(self.id, data)
        return True

    def read(self) -> str:
        return self._rpc.shell_read(self.id)

    def upgrade_to_meterpreter(self, local_host: str, local_port: int) -> bool:
        return self._rpc.shell_upgrade(self.id, local_host, local_port)


class MeterpreterSession(BaseSession):
    @property
    def directory_separator(self):
        return self._rpc.meterpreter_directory_separator(self.id)

    def write(self, data: str) -> bool:
        return self._rpc.meterpreter_write(self.id, data)

    def read(self) -> str:
        return self._rpc.meterpreter_read(self.id)

    def tabs(self, line: str) -> List[str]:
        return self._rpc.meterpreter_tabs(self.id, line)

    def run_single(self, data: str) -> bool:
        return self._rpc.meterpreter_run_single(self.id, data)

    def run_script(self, script_name: str) -> bool:
        return self._rpc.meterpreter_script(self.id, script_name)

    def detach(self) -> bool:
        return self._rpc.meterpreter_session_detach(self.id)

    def change_transport(self, options: MeterpreterSessionTransportOptions) -> bool:
        return self._rpc.meterpreter_transport_change(self.id, options)


class RingSession(BaseSession):
    def write(self, data: str) -> bool:
        self._rpc.ring_put(self.id, data)
        return True

    def read(self) -> str:
        return self._rpc.ring_read(self.id)


class Session(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCSession(context)

    def get(self, session_id: int) -> Union[ShellSession, MeterpreterSession, RingSession]:
        session_type = self.rpc.list_sessions()[session_id].type
        if session_type == SessionType.shell:
            return ShellSession(self.rpc, session_id)
        elif session_type == SessionType.meterpreter:
            return MeterpreterSession(self.rpc, session_id)
        else:
            return RingSession(self.rpc, session_id)

    def filter(self, options: SessionInformation, strict: bool = False) -> Dict[int, SessionInformation]:
        all_sessions = self.rpc.list_sessions()
        matched_sessions = {}
        for session_id, session_info in all_sessions.items():
            if session_info.match(options, strict):
                matched_sessions[session_id] = session_info

        return matched_sessions
