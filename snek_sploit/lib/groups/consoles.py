from snek_sploit.lib.groups.base import BaseGroup
from snek_sploit.lib.client import Client
from snek_sploit.lib.rpc import ConsoleInfo, ConsoleOptions

from typing import List, Union, Dict


class Console:
    def __init__(self, client: Client, console_id: int):
        self._client = client
        self.id = console_id

    def read(self):
        self._client.consoles.read(self.id)

    def write(self, data: str, add_new_line: bool = True):
        self._client.consoles.write(self.id, data, add_new_line)

    def destroy(self):
        self._client.consoles.destroy(self.id)

    def tabs(self, line: str):
        self._client.consoles.tabs(self.id, line)


class Consoles(BaseGroup):
    def create(self):
        console_info = self._client.consoles.create()
        return Console(self._client, console_info.id)
