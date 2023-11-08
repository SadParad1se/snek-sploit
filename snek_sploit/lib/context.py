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
        # MSF self-signed certificate;
        # TODO: https://github.com/rapid7/metasploit-framework/issues/15569#issuecomment-901158008
        #  From the msfrpc -h ...
        #  -c   (JSON-RPC) Path to certificate (default: /root/.msf4/msf-ws-cert.pem)
        # TODO: Optionally allow ignoring of the cert
        #  https://stackoverflow.com/a/28002687
        self.certificate = certificate if certificate != "" else False

        self.token = token

    def call(self, endpoint: str, arguments: list = None) -> dict:
        if arguments is None:
            arguments = []

        if endpoint != api.AUTH_LOGIN:
            arguments = [self.token, *arguments]

        data = msgpack.dumps([endpoint, *arguments])
        request = requests.post(self.url, data, headers=self.headers, verify=self.certificate)
        return msgpack.loads(request.content)
