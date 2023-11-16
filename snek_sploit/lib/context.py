import requests
import msgpack
from typing import Union

from snek_sploit.util import constants


class Context:
    def __init__(self, username: str, password: str, host: str = "127.0.0.1", port: int = 55553, uri: str = "/api/",
                 ssl: bool = True, certificate: str = "", token: str = "", timeout: Union[float, tuple] = None):
        self.username = username
        self.password = password
        self.token = token

        self._url = f"http{'s' if ssl else ''}://{host}:{port}{uri}"
        self._headers = {"Content-type": "binary/message-pack"}
        self.timeout = timeout
        # MSF self-signed certificate
        # TODO: https://github.com/rapid7/metasploit-framework/issues/15569#issuecomment-901158008
        #  From the msfrpc -h ...
        #  -c   (JSON-RPC) Path to certificate (default: /root/.msf4/msf-ws-cert.pem)
        self._certificate = certificate if certificate != "" else False

    def _create_arguments(self, call_arguments: list, use_token: bool) -> list:
        arguments = [self.token] if use_token else []

        if call_arguments is not None:
            arguments += call_arguments

        return arguments

    def call(self, endpoint: str, arguments: list = None, use_token: bool = True,
             timeout: Union[float, tuple] = None) -> Union[dict, str]:
        if timeout is None:
            timeout = self.timeout

        data = msgpack.dumps([endpoint, *self._create_arguments(arguments, use_token)])
        request = requests.post(self._url, data, headers=self._headers, verify=self._certificate, timeout=timeout)
        response = msgpack.loads(request.content, strict_map_key=False)
        print(response)  # TODO: remove, only for quick and dirty debugging

        if isinstance(response, dict) and response.get(constants.ERROR) is not None:
            raise Exception(response)

        return response
