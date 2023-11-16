from typing import List, Dict

from snek_sploit.lib.base import Base
from snek_sploit.util import constants


# TODO unfinished, untested
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

    def list_sessions(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.LIST, list(args))

        return response

    def stop(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.STOP, list(args))

        return response

    def shell_read(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.SHELL_READ, list(args))

        return response

    def shell_write(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.SHELL_WRITE, list(args))

        return response

    def shell_upgrade(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.SHELL_UPGRADE, list(args))

        return response

    def meterpreter_read(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_READ, list(args))

        return response

    def meterpreter_write(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_WRITE, list(args))

        return response

    def meterpreter_session_detach(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SESSION_DETACH, list(args))

        return response

    def meterpreter_session_kill(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SESSION_KILL, list(args))

        return response

    def meterpreter_tabs(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_TABS, list(args))

        return response

    def meterpreter_run_single(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_RUN_SINGLE, list(args))

        return response

    def meterpreter_script(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_SCRIPT, list(args))

        return response

    def meterpreter_transport_change(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_TRANSPORT_CHANGE, list(args))

        return response

    def meterpreter_directory_separator(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.METERPRETER_DIRECTORY_SEPARATOR, list(args))

        return response

    def compatible_modules(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.COMPATIBLE_MODULES, list(args))

        return response

    def ring_read(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.RING_READ, list(args))

        return response

    def ring_put(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.RING_PUT, list(args))

        return response

    def ring_last(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.RING_LAST, list(args))

        return response

    def ring_clear(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.RING_CLEAR, list(args))

        return response
