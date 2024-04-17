from requests import ReadTimeout
from dataclasses import dataclass
from typing import Union, Dict

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants, exceptions


@dataclass
class ModuleStatistics:
    """
    Number of installed modules.
    """

    exploits: int
    auxiliary: int
    post: int
    encoders: int
    nops: int
    payloads: int
    evasions: int


@dataclass
class VersionInformation:
    """
    Information about framework versions.
    """

    version: str
    ruby: str
    api: str


@dataclass
class FrameworkThread:
    """
    Information about framework thread.
    """

    status: str
    critical: bool
    name: str
    started: str


class RPCCore(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Core.html
    """

    VERSION = "core.version"
    STOP = "core.stop"
    GETG = "core.getg"
    SETG = "core.setg"
    UNSETG = "core.unsetg"
    SAVE = "core.save"
    MODULE_STATS = "core.module_stats"
    ADD_MODULE_PATH = "core.add_module_path"
    RELOAD_MODULES = "core.reload_modules"
    THREAD_LIST = "core.thread_list"
    THREAD_KILL = "core.thread_kill"

    @staticmethod
    def _parse_version(response: Dict[bytes, Union[bytes, str]]) -> VersionInformation:
        """
        Get versions from the response.
        :param response: API response containing the necessary data
        :return: Parsed version information
        """
        return VersionInformation(
            response[constants.B_VERSION], response[constants.B_RUBY].decode(), response[constants.B_API].decode()
        )

    @staticmethod
    def _parse_module_statistics(response: Dict[bytes, int]) -> ModuleStatistics:
        """
        Get module statistics from the response.
        :param response: API response containing the necessary data
        :return: Parsed module statistics
        """
        return ModuleStatistics(
            response[constants.B_EXPLOITS],
            response[constants.B_AUXILIARY],
            response[constants.B_POST],
            response[constants.B_ENCODERS],
            response[constants.B_NOPS],
            response[constants.B_PAYLOADS],
            response[constants.B_EVASIONS],
        )

    @staticmethod
    def _parse_framework_thread(response: Dict[str, Union[bytes, str, bool]]) -> FrameworkThread:
        """
        Get framework thread from the response.
        :param response: API response containing the necessary data
        :return: Parsed framework thread information
        """
        return FrameworkThread(
            response[constants.STATUS].decode(),
            response[constants.CRITICAL],
            response[constants.NAME],
            response[constants.STARTED],
        )

    def version(self) -> VersionInformation:
        """
        Get the RPC service versions.
        :return: RPC service versions
        :full response example:
            {b'version': '6.3.31-dev', b'ruby': b'3.0.5 x86_64-linux-musl 2022-11-24', b'api': b'1.0'}
        """
        response = self._context.call(self.VERSION)

        return self._parse_version(response)

    def stop(self) -> None:
        """
        Stops the RPC service.
        :return: None
        :full response example: No response
        """
        context_timeout = self._context.timeout
        timeout = (context_timeout[0] if isinstance(context_timeout, tuple) else context_timeout, 0.001)

        try:
            self._context.call(self.STOP, timeout=timeout)
        except ReadTimeout:
            pass

    def global_get(self, variable: str) -> str:
        """
        Get a global datastore option (variable).
        :param variable: Name of the variable
        :return: Value of the variable (empty string in case it doesn't exist)
        :full response example: {b'ASD': b'dsa'}
        :undefined variable response example: {b'ASD': ''}
        """
        variable = variable.upper()

        response = self._context.call(self.GETG, [variable])

        value = response[variable.encode()]
        if value == "":
            raise exceptions.InputError("Undefined variable")

        return value.decode()

    def global_set(self, variable: str, value: str) -> bool:
        """
        Set a global datastore option (variable).
        :param variable: Name of the variable
        :param value: Value of the variable
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        variable = variable.upper()

        response = self._context.call(self.SETG, [variable, value])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def global_unset(self, variable: str) -> bool:
        """
        Unset a global datastore option (variable).
        :param variable: Name of the variable
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        variable = variable.upper()

        response = self._context.call(self.UNSETG, [variable])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def save(self) -> bool:
        """
        Save current framework settings.
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.SAVE)

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def module_stats(self) -> ModuleStatistics:
        """
        Get module stats.
        :return: Module statistics
        :full response example:
            {b'exploits': 2346, b'auxiliary': 1220, b'post': 413, b'encoders': 46, b'nops': 11, b'payloads': 1387,
             b'evasions': 9}
        """
        response = self._context.call(self.MODULE_STATS)

        return self._parse_module_statistics(response)

    def add_module_path(self, path: str) -> ModuleStatistics:
        """
        Add a new local file system path (local to the server) as a module path.
        :param path: Path to load
        :return: Module statistics
        :full response example:
            {b'exploits': 2346, b'auxiliary': 1220, b'post': 413, b'encoders': 46, b'nops': 11, b'payloads': 1387,
             b'evasions': 9}
        """
        response = self._context.call(self.ADD_MODULE_PATH, [path])

        return self._parse_module_statistics(response)

    def reload_modules(self) -> ModuleStatistics:
        """
        Reload framework modules.
        :return: Module statistics
        :full response example:
            {b'exploits': 2346, b'auxiliary': 1220, b'post': 413, b'encoders': 46, b'nops': 11, b'payloads': 1387,
             b'evasions': 9}
        """
        response = self._context.call(self.RELOAD_MODULES)

        return self._parse_module_statistics(response)

    def thread_list(self) -> Dict[int, FrameworkThread]:  # TODO: Move the id to the thread and make it a list?
        """
        List framework threads.
        :return: List of framework threads
        :full response example:
            {0: {'status': b'sleep', 'critical': True, 'name': 'MetasploitRPCServer',
                 'started': '2023-11-13 08:47:35 +0000'}}
        """
        response = self._context.call(self.THREAD_LIST)

        return {thread_id: self._parse_framework_thread(thread) for thread_id, thread in response.items()}

    def thread_kill(self, thread_id: int) -> bool:
        """
        Kill a framework thread.
        :param thread_id: ID of the thread
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.THREAD_KILL, [thread_id])

        return response[constants.B_RESULT] == constants.B_SUCCESS


class Core(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCCore(context)
