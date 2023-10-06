import requests
import msgpack

from snek_sploit.util import api


class Client:
    def __init__(self, username: str, password: str, host: str = "127.0.0.1", port: int = 55553, uri: str = "/api/",
                 ssl: bool = True, certificate: str = "", log_in: bool = True):
        self._username = username
        self._password = password

        self._url = f"http{'s' if ssl else ''}://{host}:{port}{uri}"
        self._headers = {"Content-type": "binary/message-pack"}
        self._certificate = certificate if certificate != "" else False  # MSF self-signed certificate; Where to get it?

        self._token = self._login() if log_in else ""

    def _login(self):
        response = self.call(api.AUTH_LOGIN, [self._username, self._password])

        if response[b"result"] == b"success":
            # TODO: save a token to the DB since it will be removed in 5 minutes; allow user to not create perm token?
            return response[b"token"].decode()

        raise Exception("Unable to login")

    def login(self):
        self._token = self._login()

    def call(self, endpoint: str, arguments: list = None):
        if arguments is None:
            arguments = []

        if endpoint != api.AUTH_LOGIN:
            arguments = [self._token, *arguments]

        data = msgpack.dumps([endpoint, *arguments])
        request = requests.post(self._url, data, headers=self._headers, verify=self._certificate)
        return msgpack.loads(request.content)
