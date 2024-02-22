from abc import ABC, abstractmethod
from typing import List, Union, Dict
import time

from snek_sploit.lib.groups.base import BaseGroup
from snek_sploit.lib.client import Client
from snek_sploit.lib.rpc import SessionInformation, MeterpreterSessionTransportOptions
from snek_sploit.util import SessionType


class Session(ABC):
    def __init__(self, client: Client, session_id: int, info: SessionInformation = None):
        self._client = client
        self.id = session_id
        try:
            self.info = info if info is not None else self.fetch_information()
        except Exception:
            raise Exception(f"Unable to fetch information about the session with id {self.id}. Make sure it exists.")

    def fetch_information(self) -> SessionInformation:
        return self._client.sessions.list_sessions()[self.id]

    def kill(self) -> bool:
        return self._client.sessions.stop(self.id)

    def compatible_post_modules(self):
        return self._client.sessions.compatible_modules(self.id)

    @abstractmethod
    def write(self, data: str) -> bool:
        pass

    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def execute(self, command: str, minimal_execution_time: float, timeout: float, success_flags: List[str],
                reading_delay: float) -> str:
        pass

    def gather_output(self, minimal_execution_time: float = 3, timeout: float = None, success_flags: List[str] = None,
                      reading_delay: float = 1) -> str:
        """
        Gather output from the session.
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

    def clear_buffer(self) -> None:
        """
        Clear unread data from the session.
        :return: None
        """
        self.read()


class SessionShell(Session):
    def write(self, data: str) -> bool:
        self._client.sessions.shell_write(self.id, data)
        return True

    def read(self) -> str:
        return self._client.sessions.shell_read(self.id)

    def upgrade_to_meterpreter(self, local_host: str, local_port: int, payload: str = None) -> bool:
        # TODO: Custom update_to_meterpreter implementation? https://github.com/rapid7/metasploit-framework/issues/8800
        #  The current one fails since its unable to use x64 instead of x86 architecture, we could add an optional
        #  payload argument, which would mitigate this issue partially
        if payload is None:
            return self._client.sessions.shell_upgrade(self.id, local_host, local_port)

        # TODO: set PAYLOAD_OVERRIDE: linux/x64/meterpreter/reverse_tcp,
        #  module: post/multi/manage/shell_to_meterpreter
        return False

    def execute(self, command: str, minimal_execution_time: float = 3, timeout: float = None,
                success_flags: List[str] = None, reading_delay: float = 1) -> str:
        self.clear_buffer()
        self.write(command)

        return self.gather_output(minimal_execution_time, timeout, success_flags, reading_delay)


class SessionMeterpreter(Session):
    # TODO: execute and execute_in_shell are partially finished, since they have to be tested with the x64 payload.
    #   If it works seamlessly, then good. However, even if it works, try to play with the run_single and channel
    #   combination a bit more. Also, make sure to remove the process ID, or save it into memory or return it. Right
    #   now it poisons the command output.
    @property
    def directory_separator(self):
        return self._client.sessions.meterpreter_directory_separator(self.id)

    def write(self, data: str) -> bool:
        return self._client.sessions.meterpreter_write(self.id, data)

    def read(self) -> str:
        return self._client.sessions.meterpreter_read(self.id)

    def tabs(self, line: str) -> List[str]:
        return self._client.sessions.meterpreter_tabs(self.id, line)

    def run_single(self, data: str) -> bool:
        return self._client.sessions.meterpreter_run_single(self.id, data)

    def run_script(self, script_name: str) -> bool:
        return self._client.sessions.meterpreter_script(self.id, script_name)

    def detach(self) -> bool:
        return self._client.sessions.meterpreter_session_detach(self.id)

    def change_transport(self, options: MeterpreterSessionTransportOptions) -> bool:
        return self._client.sessions.meterpreter_transport_change(self.id, options)

    def execute(self, command: str, minimal_execution_time: float = 3, timeout: float = None,
                success_flags: List[str] = None, reading_delay: float = 1) -> str:
        self.clear_buffer()
        self.write(command)

        return self.gather_output(minimal_execution_time, timeout, success_flags, reading_delay)

    def execute_in_shell(self, command: str, arguments: List[str], minimal_execution_time: float = 3,
                         timeout: float = None, success_flags: List[str] = None, reading_delay: float = 1) -> str:
        self.clear_buffer()

        # TODO: test with custom x64 payload
        self.run_single(f"execute -f {command} -c -i -a {' '.join(arguments)}")

        return self.gather_output(minimal_execution_time, timeout, success_flags, reading_delay)


class SessionRing(Session):
    def write(self, data: str) -> bool:
        self._client.sessions.ring_put(self.id, data)
        return True

    def read(self) -> str:
        return self._client.sessions.ring_read(self.id)

    def execute(self, command: str, minimal_execution_time: float = 3, timeout: float = None,
                success_flags: List[str] = None, reading_delay: float = 1) -> str:
        self.clear_buffer()
        self.write(command)

        return self.gather_output(minimal_execution_time, timeout, success_flags, reading_delay)


class Sessions(BaseGroup):
    def get(self, session_id: int) -> Union[SessionShell, SessionMeterpreter, SessionRing]:
        session_info = self._client.sessions.list_sessions()[session_id]
        session_type = session_info.type
        if session_type == SessionType.shell:
            return SessionShell(self._client.sessions, session_id, session_info)
        elif session_type == SessionType.meterpreter:
            return SessionMeterpreter(self._client.sessions, session_id, session_info)
        else:
            return SessionRing(self._client.sessions, session_id, session_info)

    def all(self) -> Dict[int, SessionInformation]:
        return self._client.sessions.list_sessions()

    def filter(self, options: SessionInformation, strict: bool = False) -> Dict[int, SessionInformation]:
        all_sessions = self._client.sessions.list_sessions()
        matched_sessions = {}
        for session_id, session_info in all_sessions.items():
            if session_info.match(options, strict):
                matched_sessions[session_id] = session_info

        return matched_sessions
