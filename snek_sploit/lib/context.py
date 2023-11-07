import requests
import msgpack

from snek_sploit.util import api


class Context:
    def __init__(self, username: str, password: str, host: str = "127.0.0.1", port: int = 55553, uri: str = "/api/",
                 ssl: bool = True, certificate: str = "", token: str = ""):
        self.username = username
        self.password = password

        self.url = f"http{'s' if ssl else ''}://{host}:{port}{uri}"
        self.headers = {"Content-type": "binary/message-pack"}
        self.certificate = certificate if certificate != "" else False  # MSF self-signed certificate; Where to get it?

        self.token = token

    def call(self, endpoint: str, arguments: list = None) -> dict:
        if arguments is None:
            arguments = []

        if endpoint != api.AUTH_LOGIN:
            arguments = [self.token, *arguments]

        data = msgpack.dumps([endpoint, *arguments])
        request = requests.post(self.url, data, headers=self.headers, verify=self.certificate)
        return msgpack.loads(request.content)
