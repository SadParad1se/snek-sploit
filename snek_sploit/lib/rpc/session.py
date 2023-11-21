from typing import List, Dict, Union
from dataclasses import dataclass, asdict

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
        arch: Platform/Architecture
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
    arch: str


@dataclass
class MeterpreterSessionTransportOptions:
    """
    Options used to set up the transport for a Meterpreter session.

    Parameters:
        transport: The transport protocol to use (e.g. reverse_tcp, reverse_http, bind_tcp etc)
        lhost: The LHOST of the listener to use
        lport: The LPORT of the listener to use
        ua: The User Agent String to use for reverse_http(s)
        proxy_host: The address of the proxy to route transport through
        proxy_port: The port the proxy is listening on
        proxy_type: The type of proxy to use
        proxy_user: The username to authenticate to the proxy with
        proxy_pass: The password to authenticate to the proxy with
        comm_timeout: Connection timeout in seconds
        session_exp: Session Expiration Timeout
        retry_total: Total number of times to retry establishing the transport
        retry_wait: The number of seconds to wait between retries
        cert: Path to the SSL Cert to use for HTTPS
    """
    transport: str
    lhost: str
    lport: str
    ua: str
    proxy_host: str
    proxy_port: str
    proxy_type: str
    proxy_user: str
    proxy_pass: str
    comm_timeout: str
    session_exp: str
    retry_total: str
    retry_wait: str
    cert: str


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

    def _parse_session_information(self, response: Dict[str, Union[bytes, str, int]]) -> SessionInformation:
        parsed_response = self.decode(response)
        return SessionInformation(
            parsed_response[constants.TYPE],
            parsed_response[constants.TUNNEL_LOCAL],
            parsed_response[constants.TUNNEL_PEER],
            parsed_response[constants.VIA_EXPLOIT],
            parsed_response[constants.DESC],
            parsed_response[constants.INFO],
            parsed_response[constants.WORKSPACE],
            parsed_response[constants.SESSION_HOST],
            parsed_response[constants.SESSION_PORT],
            parsed_response[constants.TARGET_HOST],
            parsed_response[constants.USERNAME],
            parsed_response[constants.UUID],
            parsed_response[constants.EXPLOIT_UUID],
            parsed_response[constants.ROUTES],
            parsed_response[constants.ARCH]
        )

    def list_sessions(self) -> Dict[int, SessionInformation]:
        """
        Get a list of sessions that belong to the framework instance used by the RPC service.
        :return: Existing sessions
        :full response example:
            {1: {b'type': b'shell', b'tunnel_local': b'192.168.0.222:4444', b'tunnel_peer': b'192.168.0.222:43736',
             b'via_exploit': b'exploit/multi/handler', b'via_payload': b'payload/python/shell_reverse_tcp',
             b'desc': b'Command shell', b'info': b'', b'workspace': b'default', b'session_host': b'192.168.0.222',
             b'session_port': 43736, b'target_host': '', b'username': b'unknown', b'uuid': b'5wcqy12v',
             b'exploit_uuid': b'ffpazxus', b'routes': '', b'arch': b'python'}}
        """
        response = self._context.call(self.LIST)

        return {key: self._parse_session_information(value) for key, value in response.items()}

    def stop(self, session_id: int) -> bool:
        """
        Stop a session - alias for killing a session in msfconsole.
        :param session_id: ID of the session
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.STOP, [session_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def shell_read(self, session_id: int, pointer: int = None) -> object:  # TODO
        """
        Read the output of a shell session (such as a command output).
        :param session_id: ID of the session
        :param pointer: Read from/Offset?  # TODO
        :return:
        :full response example:
        """
        response = self._context.call(self.SHELL_READ, [session_id, pointer])

        return response

    def shell_write(self, session_id: int, data: str, add_new_line: bool = True) -> int:  # TODO
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

    def shell_upgrade(self, session_id: int, local_host: str, local_port: int) -> bool:  # TODO
        """
        Upgrade a shell to a meterpreter.
        This uses post/multi/manage/shell_to_meterpreter.
        :param session_id: ID of the session
        :param local_host: Local host
        :param local_port: Local port
        :return: True in case of success
        :full response example:
        """
        response = self._context.call(self.SHELL_UPGRADE, [session_id, local_host, local_port])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_read(self, session_id: int) -> object:  # TODO
        """
        Get the output from a meterpreter session (such as a command output).
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_READ, [session_id])

        return response

    def meterpreter_write(self, session_id: int, data: str) -> bool:  # TODO
        """
        Write an input to a meterpreter prompt.
        :param session_id: ID of the session
        :param data: Data (command) to write
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_WRITE, [session_id, data])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_session_detach(self, session_id: int) -> object:  # TODO
        """
        Detach from a meterpreter session. Serves the same purpose as CTRL+Z.
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SESSION_DETACH, [session_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_session_kill(self, session_id: int) -> object:  # TODO
        """
        Kill a meterpreter session. Serves the same purpose as CTRL+C.
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SESSION_KILL, [session_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_tabs(self, session_id: int, line: str) -> object:  # TODO
        """

        :param session_id: ID of the session
        :param line: Line you want to complete
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_TABS, [session_id, line])

        return response

    def meterpreter_run_single(self, session_id: int, data: str) -> object:  # TODO
        """
        Run a meterpreter command even if interacting with a shell or other channel.
        :param session_id: ID of the session
        :param data: Data (command) to write
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_RUN_SINGLE, [session_id, data])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_script(self, session_id: int, script_name: str) -> object:  # TODO
        """
        !!!DEPRECATED!!!  # TODO: remove?
        """
        response = self._context.call(self.METERPRETER_SCRIPT, [session_id, script_name])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_transport_change(self, session_id: int, options: MeterpreterSessionTransportOptions) -> object:  # TODO
        """
        Change the Transport of a given Meterpreter Session.
        :param session_id: ID of the session
        :param options: Options for the Meterpreter session transport
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_TRANSPORT_CHANGE, [session_id, asdict(options)])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def meterpreter_directory_separator(self, session_id: int) -> object:  # TODO
        """
        Get the separator used by the meterpreter.
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_DIRECTORY_SEPARATOR, [session_id])

        return response

    def compatible_modules(self, session_id: int) -> List[str]:
        """
        Get the compatible post modules for this session.
        :param session_id: ID of the session
        :return: Compatible modules
        :full response example: {b'modules': [b'post/multi/recon/local_exploit_suggester']}
        """
        response = self._context.call(self.COMPATIBLE_MODULES, [session_id])

        return [each.decode() for each in response[constants.B_MODULES]]

    def ring_read(self, session_id: int) -> object:  # TODO
        """
        Read the output of a shell session (such as a command output).
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_READ, [session_id])

        return response

    def ring_put(self, session_id: int, data: str) -> object:  # TODO
        """
        Write to a shell session (such as a command).
        :param session_id: ID of the session
        :param data: Data (command) to write
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_PUT, [session_id, data])

        return response

    def ring_last(self, session_id: int) -> object:  # TODO
        """
        Get the last sequence (last issued ReadPointer) for a shell session.
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_LAST, [session_id])

        return response

    def ring_clear(self, session_id: int) -> object:  # TODO
        """
        Clear a shell session. This may be useful to reclaim memory for idle background sessions.
        :param session_id: ID of the session
        :return:
        :full response example:
        """
        response = self._context.call(self.RING_CLEAR, [session_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS
