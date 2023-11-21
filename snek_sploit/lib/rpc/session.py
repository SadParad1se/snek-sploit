from typing import List, Dict
from dataclasses import dataclass

from snek_sploit.lib.base import Base
from snek_sploit.util import constants


@dataclass
class SessionInformation:
    """
    Information about a session.

    Parameters:
        type: Payload type. Example: meterpreter
        tunnel_local: Tunnel (where the malicious traffic comes from)
        tunnel_peer: Tunnel (local)
        via_exploit: Name of the exploit used by the session
        desc: Session description
        info: Session info (most likely the target's computer name)
        workspace: Name of the workspace
        session_host: Session host
        session_port: Session port
        target_host: Target host
        username: Username
        uuid: UUID
        exploit_uuid: Exploit's UUID
        routes: Routes
        platform: Platform
    """
    type: str
    tunnel_local: str
    tunnel_peer: str
    via_exploit: str
    desc: str
    info: str
    workspace: str
    session_host: str
    session_port: int
    target_host: str
    username: str
    uuid: str
    exploit_uuid: str
    routes: str
    platform: str


class RPCSession(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Session.html
    """
    LIST = "session.list"
    STOP = "session.stop"
    SHELL_READ = "session.shell_read"
    SHELL_WRITE = "session.shell_write"
    SHELL_UPGRADE = "session.shell_upgrade"
    METERPRETER_READ = "session.meterpreter_read"
    METERPRETER_WRITE = "session.meterpreter_write"
    METERPRETER_SESSION_DETACH = "session.meterpreter_session_detach"
    METERPRETER_SESSION_KILL = "session.meterpreter_session_kill"
    METERPRETER_TABS = "session.meterpreter_tabs"
    METERPRETER_RUN_SINGLE = "session.meterpreter_run_single"
    METERPRETER_SCRIPT = "session.meterpreter_script"
    METERPRETER_TRANSPORT_CHANGE = "session.meterpreter_transport_change"
    METERPRETER_DIRECTORY_SEPARATOR = "session.meterpreter_directory_separator"
    COMPATIBLE_MODULES = "session.compatible_modules"
    RING_READ = "session.ring_read"
    RING_PUT = "session.ring_put"
    RING_LAST = "session.ring_last"
    RING_CLEAR = "session.ring_clear"

    @staticmethod
    def _parse_session_information(response: Dict[str, str]) -> SessionInformation:
        return SessionInformation(
            response[constants.B_TYPE]
        )

    def list_sessions(self) -> Dict[int, SessionInformation]:
        """
        Get a list of sessions that belong to the framework instance used by the RPC service.
        :return: Available sessions
        :full response example:
        """
        response = self._context.call(self.LIST)

        return {key: self._parse_session_information(value) for key, value in response.items()}

    def stop(self, session_id: int) -> bool:
        """
        Stop a session - alias for killing a session in msfconsole.
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.STOP, [session_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def shell_read(self, session_id: int, pointer: int = None) -> object:
        """
        Read the output of a shell session (such as a command output).
        :param session_id: ID of the session
        :param pointer: Read from/Offset?  # TODO
        :return:
        :full response example:
        """
        response = self._context.call(self.SHELL_READ, [session_id, pointer])

        return response

    def shell_write(self, session_id: int, data: str, add_new_line: bool = True) -> object:
        """
        Write to a shell session (such as a command).
        Note that you will to manually add a newline at the enf of your input so the system will process it.
        :param session_id: ID of the session
        :param data: Data (command) to write
        :param add_new_line: Whether to add a new line at the end of the data
        :return:
        :full response example:
        """
        if add_new_line:
            data += "\r\n"

        response = self._context.call(self.SHELL_WRITE, [session_id, data])

        return response

    def shell_upgrade(self, session_id: int, local_host: str, local_port: int) -> object:
        """

        :param session_id: ID of the session
        :param local_host: Local host
        :param local_port: Local port
        :return:
        :full response example:
        """
        response = self._context.call(self.SHELL_UPGRADE, list(args))

        return response

    def meterpreter_read(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_READ, list(args))

        return response

    def meterpreter_write(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_WRITE, list(args))

        return response

    def meterpreter_session_detach(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SESSION_DETACH, list(args))

        return response

    def meterpreter_session_kill(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SESSION_KILL, list(args))

        return response

    def meterpreter_tabs(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_TABS, list(args))

        return response

    def meterpreter_run_single(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_RUN_SINGLE, list(args))

        return response

    def meterpreter_script(self, session_id: int, data: ) -> object:
        """
        !!!DEPRECATED!!!  # TODO: remove?
        """
        response = self._context.call(self.METERPRETER_SCRIPT, list(args))

        return response

    def meterpreter_transport_change(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_TRANSPORT_CHANGE, list(args))

        return response

    def meterpreter_directory_separator(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_DIRECTORY_SEPARATOR, list(args))

        return response

    def compatible_modules(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.COMPATIBLE_MODULES, list(args))

        return response

    def ring_read(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_READ, list(args))

        return response

    def ring_put(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_PUT, list(args))

        return response

    def ring_last(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_LAST, list(args))

        return response

    def ring_clear(self, session_id: int) -> object:
        """

        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_CLEAR, list(args))

        return response
