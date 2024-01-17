from snek_sploit.lib.client import Client


class BaseGroup:
    def __init__(self, client: Client):
        self._client = client
