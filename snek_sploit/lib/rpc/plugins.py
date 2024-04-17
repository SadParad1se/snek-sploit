from typing import List

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants


class RPCPlugins(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Plugin.html
    """

    LOAD = "plugin.load"
    UNLOAD = "plugin.unload"
    LOADED = "plugin.loaded"

    def load(self, name: str, options: dict = None) -> bool:
        """
        Load a plugin.
        :param name: Plugin filename (without the extension)
        :param options: Options to pass to the plugin
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        if options is None:
            options = {}

        response = self._context.call(self.LOAD, [name, options])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def unload(self, name: str) -> bool:
        """
        Unload a plugin.
        :param name: Plugin filename (without the extension)
        :return: True in case of success
        :full response example: {b'result': b'success'}
        """
        response = self._context.call(self.UNLOAD, [name])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def list_loaded(self) -> List[str]:
        """
        List loaded plugins.
        :return: List of loaded plugins
        :full response example: {'plugins': ['msgrpc']}
        """
        response = self._context.call(self.LOADED)

        return response[constants.PLUGINS]


class Plugins(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCPlugins(context)
