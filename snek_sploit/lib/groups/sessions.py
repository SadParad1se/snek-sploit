from abc import ABC, abstractmethod
from typing import List, Union, Dict
import time

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

    def gather_output(self, minimal_execution_time: float = 3, timeout: float = None, success_flags: List[str] = None,
                      reading_delay: float = 1) -> str:
        """
        Gather output from the shell.
        :param minimal_execution_time: The minimum amount of seconds to wait before exiting in case no output is read
        :param timeout: The maximum time to wait for the output
        :param success_flags: Flags to indicate the gathered output is enough (one flag == stop gathering)
        :param reading_delay: Delay between the readings
        :return: Gathered output
        """
        output = ""
        timestamp = time.time()

        if timeout:
            timeout = timestamp + max(timeout, minimal_execution_time)

        minimal_execution_time = timestamp + minimal_execution_time

        while (data := self.read()) or (time.time() < minimal_execution_time):
            output += data

            # TODO: switch to regex?
            # TODO: make sure at least the last 200 characters are tested, since the data can be split randomly?
            if success_flags and any(flag in data for flag in success_flags):
                break

            if timeout and time.time() >= timeout:
                break

            time.sleep(reading_delay)

        return output

    def execute(self, command: str, minimal_execution_time: float = 3, timeout: float = None,
                success_flags: List[str] = None, reading_delay: float = 1) -> str:
        self.read()  # Clean the shell in case there are any unread data
        self.write(command)

        return self.gather_output(minimal_execution_time, timeout, success_flags, reading_delay)


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


class Sessions(ContextBase):
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

    def all(self) -> Dict[int, SessionInformation]:
        return self.rpc.list_sessions()

    def filter(self, options: SessionInformation, strict: bool = False) -> Dict[int, SessionInformation]:
        all_sessions = self.rpc.list_sessions()
        matched_sessions = {}
        for session_id, session_info in all_sessions.items():
            if session_info.match(options, strict):
                matched_sessions[session_id] = session_info

        return matched_sessions
