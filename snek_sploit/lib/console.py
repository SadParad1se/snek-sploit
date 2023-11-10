from dataclasses import dataclass

from snek_sploit.lib.base import Base
from snek_sploit.util import api, constants


@dataclass
class ConsoleInfo:
    id: str
    prompt: bytes
    busy: bool
    data: bytes


class Console(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Console.html
    """
    @staticmethod
    def _parse_console_data(response: dict) -> ConsoleInfo:
        """

        :param response:
        :return:
        """
        return ConsoleInfo(
            response.get(constants.ID),
            response[constants.PROMPT],
            response[constants.BUSY],
            response.get(constants.DATA)
        )

    def create(self, options: dict = None) -> ConsoleInfo:
        """

        :param options:
        :return:
        :full response example: {b'id': '3', b'prompt': b'', b'busy': False}
        """
        # TODO: what options are supported?
        #  https://github.com/rapid7/metasploit-framework/blob/6659684fdf9e669b786c2ec15007b15d56219c4c/lib/msf/ui/web/web_console.rb#L46C10-L46C10
        if options is None:
            options = {}

        response = self._context.call(api.CONSOLE_CREATE, [options])

        return self._parse_console_data(response)

    def list_consoles(self) -> list[ConsoleInfo]:
        """

        :return:
        :full response example: {b'consoles': [{b'id': '1', b'prompt': b'msf6 > ', b'busy': False}]}
        """
        response = self._context.call(api.CONSOLE_LIST)

        consoles = []
        for console in response[constants.CONSOLES]:
            consoles.append(self._parse_console_data(console))

        return consoles

    def destroy(self, console_id: int) -> bool:
        """

        :param console_id:
        :return:
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(api.CONSOLE_DESTROY, [console_id])

        if response[constants.RESULT] == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.RESULT] == constants.SUCCESS

    def read(self, console_id: int) -> ConsoleInfo:
        """

        :param console_id:
        :return:
        :full response example: {b'data': b"... https://docs.metasploit.com/\n\n", b'prompt': b'msf6 > ', b'busy': True}
        """
        response = self._context.call(api.CONSOLE_READ, [console_id])

        if response.get(constants.RESULT) == constants.FAILURE:
            raise Exception("Invalid console ID")

        return self._parse_console_data(response)

    def write(self, console_id: int, data: str) -> int:
        """

        :param console_id:
        :param data:
        :return:
        :full response example: {b'wrote': 11}
        """
        data += "\r\n"

        response = self._context.call(api.CONSOLE_WRITE, [console_id, data])

        if response.get(constants.RESULT) == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.WROTE]

    def tabs(self, console_id: int, line: str) -> list[bytes]:
        """

        :param console_id:
        :param line:
        :return:
        :full response example: {b'tabs': [b'use exploit/windows/smb/ms08_067_netapi']}
        """
        response = self._context.call(api.CONSOLE_TABS, [console_id, line])

        if response.get(constants.RESULT) == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.TABS]

    def session_kill(self, console_id: int) -> bool:
        """

        :param console_id:
        :return:
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(api.CONSOLE_SESSION_KILL, [console_id])

        if response[constants.RESULT] == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.RESULT] == constants.SUCCESS

    def session_detach(self, console_id: int) -> bool:
        """

        :param console_id:
        :return:
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(api.CONSOLE_SESSION_DETACH, [console_id])

        if response[constants.RESULT] == constants.FAILURE:
            raise Exception("Invalid console ID")

        return response[constants.RESULT] == constants.SUCCESS
