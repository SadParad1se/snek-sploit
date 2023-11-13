from dataclasses import dataclass

from snek_sploit.lib.base import Base
from snek_sploit.util import constants


@dataclass
class ConsoleInfo:
    id: str
    prompt: bytes
    busy: bool


@dataclass
class ConsoleData:
    prompt: bytes
    busy: bool
    data: bytes


class RPCConsole(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Console.html
    """
    CREATE = "console.create"
    LIST = "console.list"
    DESTROY = "console.destroy"
    READ = "console.read"
    WRITE = "console.write"
    TABS = "console.tabs"
    SESSION_KILL = "console.session_kill"
    SESSION_DETACH = "console.session_detach"

    @staticmethod
    def _parse_console_info(response: dict) -> ConsoleInfo:
        """
        Get console information from the response.
        :param response: Response containing information about the console
        :return: Information about the console
        """
        return ConsoleInfo(
            response[constants.ID],
            response[constants.PROMPT],
            response[constants.BUSY]
        )

    @staticmethod
    def _parse_console_data(response: dict) -> ConsoleData:
        """
        Get console data from the response.
        :param response: Response containing information and data about the console
        :return: Information about the console and its data
        """
        return ConsoleData(
            response[constants.PROMPT],
            response[constants.BUSY],
            response[constants.DATA]
        )

    def create(self, options: dict = None) -> ConsoleInfo:
        """
        Create a new framework console instance.
        :param options: Options used for creating the console
        :return: Information about the console
        :full response example: {b'id': '3', b'prompt': b'', b'busy': False}
        """
        # TODO: what options are supported?
        #  https://github.com/rapid7/metasploit-framework/blob/6659684fdf9e669b786c2ec15007b15d56219c4c/lib/msf/ui/web/web_console.rb#L46C10-L46C10
        if options is None:
            options = {}

        response = self._context.call(self.CREATE, [options])

        return self._parse_console_info(response)

    def list_consoles(self) -> list[ConsoleInfo]:
        """
        List framework consoles.
        :return: List of framework consoles
        :full response example: {b'consoles': [{b'id': '1', b'prompt': b'msf6 > ', b'busy': False}]}
        """
        response = self._context.call(self.LIST)

        consoles = []
        for console in response[constants.CONSOLES]:
            consoles.append(self._parse_console_info(console))

        return consoles

    def destroy(self, console_id: int) -> bool:
        """
        Delete a framework console instance.
        :param console_id: ID of the console
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.DESTROY, [console_id])

        if response[constants.RESULT] == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.RESULT] == constants.SUCCESS

    def read(self, console_id: int) -> ConsoleData:
        """
        Read output from the console.
        :param console_id: ID of the console
        :return: Output from the console
        :full response example: {b'data': b"... https://docs.metasploit.com/\n\n", b'prompt': b'msf6 > ', b'busy': True}
        """
        response = self._context.call(self.READ, [console_id])

        if response.get(constants.RESULT) == constants.FAILURE:
            raise Exception("Invalid console ID")

        return self._parse_console_data(response)

    def write(self, console_id: int, data: str) -> int:
        """
        Send an input (such as a command) to the framework console.
        :param console_id: ID of the console
        :param data: Input to be written
        :return: Number of bytes sent
        :full response example: {b'wrote': 11}
        """
        data += "\r\n"

        response = self._context.call(self.WRITE, [console_id, data])

        if response.get(constants.RESULT) == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.WROTE]

    def tabs(self, console_id: int, line: str) -> list[bytes]:
        """
        Get tab-completed version of your input (such as a module path).
        :param console_id: ID of the console
        :param line: Line you want to complete
        :return: Possible tab-completions for your input
        :full response example: {b'tabs': [b'use exploit/windows/smb/ms08_067_netapi']}
        """
        response = self._context.call(self.TABS, [console_id, line])

        if response.get(constants.RESULT) == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.TABS]

    def session_kill(self, console_id: int) -> bool:
        """
        Kill a framework session. This serves the same purpose as CTRL+C to abort an interactive session.
        Consider using the session API calls instead.
        :param console_id: ID of the console
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.SESSION_KILL, [console_id])

        if response[constants.RESULT] == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.RESULT] == constants.SUCCESS

    def session_detach(self, console_id: int) -> bool:
        """
        Detache a framework session. This serves the same purpose as CTRL+Z to background an interactive session.
        :param console_id: ID of the console
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.SESSION_DETACH, [console_id])

        if response[constants.RESULT] == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.RESULT] == constants.SUCCESS
