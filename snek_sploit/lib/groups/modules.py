from snek_sploit.lib.groups.base import BaseGroup


class Modules(BaseGroup):
    def execute(self, ):
        self._client.modules.execute()
    # TODO: use console for everything
    #  https://github.com/rapid7/metasploit-framework/issues/18241#issuecomment-1662496538
