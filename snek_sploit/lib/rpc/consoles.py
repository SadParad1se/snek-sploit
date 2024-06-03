import random
import string
from dataclasses import dataclass, asdict
from typing import List, Optional, Union
import time

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants, exceptions


@dataclass
class ConsoleInfo:
    """
    Information about the console.
    """

    id: int
    prompt: str
    busy: bool


@dataclass
class ConsoleData:
    """
    Information about the console, including returned data.
    """

    prompt: str
    busy: bool
    data: str


@dataclass
class ConsoleOptions:
    """
    Options used to initialize the console.
    Only the relevant options are mentioned here, since some are always modified by the MSF.
    Sources:
    https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/ui/web/web_console.rb#L46C10-L46C10
    https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/ui/console/driver.rb
    """

    workspace: str = None  # Use a workspace
    Readline: bool = None  # Whether to use the readline or not
    RealReadline: bool = None  # Whether to use the system's readline library instead of RBReadline
    HistFile: str = None  # Path to a file where we can store command history
    Config: str = None  # Path to the config file
    ConfirmExit: bool = None  # Whether to confirm before exiting
    XCommands: List[str] = None  # Additional startup commands
    DisableBanner: bool = None  # Whether to disable the banner on startup
    Plugins: List[str] = None  # Plugins to load


class RPCConsoles(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Console.html
    """

    CREATE = "console.create"
    DESTROY = "console.destroy"
    LIST = "console.list"
    READ = "console.read"
    WRITE = "console.write"
    TABS = "console.tabs"
    SESSION_KILL = "console.session_kill"
    SESSION_DETACH = "console.session_detach"

    @staticmethod
    def _parse_console_info(response: dict) -> ConsoleInfo:
        """
        Get console information from the response.
        :param response: API response containing the necessary data
        :return: Information about the console
        """
        return ConsoleInfo(
            int(response[constants.B_ID]), response[constants.B_PROMPT].decode(), response[constants.B_BUSY]
        )

    @staticmethod
    def _parse_console_data(response: dict) -> ConsoleData:
        """
        Get console data from the response.
        :param response: API response containing the necessary data
        :return: Information about the console and its data
        """
        return ConsoleData(
            response[constants.B_PROMPT].decode(), response[constants.B_BUSY], response[constants.B_DATA].decode()
        )

    def create(self, options: ConsoleOptions = None) -> ConsoleInfo:
        """
        Create a new framework console instance.
        :param options: Options used for creating the console
        :return: Information about the console
        :full response example: {b'id': '3', b'prompt': b'', b'busy': False}
        """
        options = asdict(options) if options is not None else {}

        response = self._context.call(self.CREATE, [options])

        return self._parse_console_info(response)

    def destroy(self, console_id: int) -> bool:
        """
        Delete a framework console instance.
        :param console_id: ID of the console
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.DESTROY, [console_id])

        if response[constants.B_RESULT] == constants.B_FAILURE:
            raise exceptions.InputError("Invalid console ID")

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def list_consoles(self) -> List[ConsoleInfo]:
        """
        List framework consoles.
        :return: List of framework consoles
        :full response example: {b'consoles': [{b'id': '1', b'prompt': b'msf6 > ', b'busy': False}]}
        """
        response = self._context.call(self.LIST)

        consoles = []
        for console in response[constants.B_CONSOLES]:
            consoles.append(self._parse_console_info(console))

        return consoles

    def read(self, console_id: int) -> ConsoleData:
        """
        Read output from the console.
        :param console_id: ID of the console
        :return: Output from the console
        :full response example: {b'data': b"... https://docs.metasploit.com/\n\n", b'prompt': b'msf6 > ', b'busy': True}
        """
        response = self._context.call(self.READ, [console_id])

        if response.get(constants.B_RESULT) == constants.B_FAILURE:
            raise exceptions.InputError("Invalid console ID")

        return self._parse_console_data(response)

    def write(self, console_id: int, data: str, add_new_line: bool = True) -> int:
        """
        Send an input (such as a command) to the framework console.
        :param console_id: ID of the console
        :param data: Input to be written
        :param add_new_line: Whether to add a new line at the end of the data
        :return: Number of bytes sent
        :full response example: {b'wrote': 11}
        """
        if add_new_line:
            data += "\r\n"

        response = self._context.call(self.WRITE, [console_id, data])

        if response.get(constants.B_RESULT) == constants.B_FAILURE:
            raise exceptions.InputError("Invalid console ID")

        return response[constants.B_WROTE]

    def tabs(self, console_id: int, line: str) -> List[str]:
        """
        Get tab-completed version of your input (such as a module path).
        :param console_id: ID of the console
        :param line: Line you want to complete
        :return: Possible tab-completions for your input
        :full response example: {b'tabs': [b'use exploit/windows/smb/ms08_067_netapi']}
        """
        response = self._context.call(self.TABS, [console_id, line])

        if response.get(constants.B_RESULT) == constants.B_FAILURE:
            raise exceptions.InputError("Invalid console ID")

        return [tab.decode() for tab in response[constants.B_TABS]]

    def session_kill(self, console_id: int) -> bool:
        """
        Kill a framework session. This serves the same purpose as CTRL+C to abort an interactive session.
        Consider using the session API calls instead.
        :param console_id: ID of the console
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.SESSION_KILL, [console_id])

        if response[constants.B_RESULT] == constants.B_FAILURE:
            raise exceptions.InputError("Invalid console ID")

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def session_detach(self, console_id: int) -> bool:
        """
        Detache a framework session. This serves the same purpose as CTRL+Z to background an interactive session.
        :param console_id: ID of the console
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.SESSION_DETACH, [console_id])

        if response[constants.B_RESULT] == constants.B_FAILURE:
            raise exceptions.InputError("Invalid console ID")

        return response[constants.B_RESULT] == constants.B_SUCCESS


class Console:
    def __init__(self, rpc: RPCConsoles, console_id: int):
        self._rpc = rpc
        self.id = console_id

    def read(self) -> ConsoleData:
        return self._rpc.read(self.id)

    def write(self, data: str, add_new_line: bool = True) -> None:
        self._rpc.write(self.id, data, add_new_line)

    def destroy(self) -> bool:
        return self._rpc.destroy(self.id)

    def tabs(self, line: str) -> List[str]:
        return self._rpc.tabs(self.id, line)

    def gather_output(
        self,
        timeout: float = None,
        reading_delay: float = 1,
        success_flags: Optional[Union[List[str], str]] = None,
        success_flag_hard_stop: bool = False,
    ) -> str:
        """
        Gather output from the console.
        :param timeout: The maximum time to wait for the output
        :param reading_delay: Delay between the readings
        :param success_flags: Flags to indicate the gathered output is enough (one flag == stop gathering)
        :param success_flag_hard_stop: Whether to exit once a success_flag is found
        :return: Gathered output
        """
        if isinstance(success_flags, str):
            success_flags = [success_flags]

        if timeout:
            timeout = time.time() + timeout

        output = ""
        end_is_nigh = False
        while (console := self.read()).busy or console.data or not output or (success_flags and not end_is_nigh):
            output += console.data

            if success_flags and any(flag in console.data for flag in success_flags):
                if success_flag_hard_stop:
                    break
                end_is_nigh = True  # In case the console is still busy, continue to gather the data

            if timeout and time.time() >= timeout:
                break

            time.sleep(reading_delay)

        return output

    def clear_buffer(self) -> None:
        """
        Clear unread data from the console.
        :return: None
        """
        self.read()

    def execute(
        self,
        command: str,
        timeout: float = None,
        reading_delay: float = 1,
        success_flags: Optional[Union[List[str], str]] = None,
        generate_success_flag: bool = True,
        success_flag_hard_stop: bool = False,
    ) -> str:
        """
        Execute a command or a set of commands (separated with `\n`) and gather it's output.
        By default, an end_check is generated and appended to the command to ensure the whole output is captured.
        :param command: Command that will be executed in the console.
        :param timeout: The maximum time to wait for the output
        :param reading_delay: Delay between the readings
        :param generate_success_flag: If `success_flags` is undefined, generate a custom one and add it to the command
        :param success_flags: Flags to indicate the gathered output is enough (one flag == stop gathering)
        :param success_flag_hard_stop: Whether to exit once a success_flag is found
        :return: Execution output
        """
        if not success_flags and generate_success_flag:
            success_flags = "".join(random.choices(string.ascii_letters + string.digits, k=20))
            command += f"\necho '{success_flags}'"

        self.clear_buffer()
        self.write(command)

        return self.gather_output(timeout, reading_delay, success_flags, success_flag_hard_stop)


class Consoles(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCConsoles(context)

    def create(self, options: ConsoleOptions = None):
        console_info = self.rpc.create(options)
        return Console(self.rpc, console_info.id)

    def all(self):
        return self.rpc.list_consoles()
