import requests
import msgpack
from abc import ABC
from typing import Union, List, Dict

from snek_sploit.util import constants, exceptions
from snek_sploit.util.retry import retry


ResponseDict = Dict[Union[int, str, bytes], Union[int, str, bytes, list, dict, bool]]
ResponseList = List[Union[str, bytes, dict]]
RPCResponse = Union[ResponseDict, str, ResponseList]


class Context:
    def __init__(
        self,
        username: str,
        password: str,
        host: str = "127.0.0.1",
        port: int = 55553,
        uri: str = "/api/",
        ssl: bool = True,
        certificate: str = "",
        token: str = "",
        timeout: Union[float, tuple] = None,
        verbose: bool = False,
    ):
        """
        Context holds information used for authentication and communication with MSF RPC.
        :param username: Username used for authentication
        :param password: Password used for authentication
        :param host: MSF RPC Host
        :param port: MSF RPC Port
        :param uri: API uri
        :param ssl: Whether the server is using SSL(TLS) or not
        :param certificate: Path to the certificate used for SSL(TLS)
        :param token: Token used for authentication
        :param timeout: Timeout for the RPC
        :param verbose: Whether to print the raw RPC response
        """
        self.username = username
        self.password = password
        self.token = token

        self._url = f"http{'s' if ssl else ''}://{host}:{port}{uri}"
        self._headers = {"Content-type": "binary/message-pack"}
        self.timeout = timeout
        self._certificate = certificate if certificate != "" else False  # MSF's self-signed certificate

        self.verbose = verbose

    def _create_arguments(self, call_arguments: list, use_token: bool) -> list:
        """
        Create arguments that will be sent to the endpoint.
        :param call_arguments: User supplied arguments
        :param use_token: Whether to use the context token or not
        :return: Endpoint arguments
        """
        arguments = [self.token] if use_token else []

        if call_arguments is not None:
            arguments += call_arguments

        return arguments

    @retry(attempts=3, on_errors=(requests.RequestException,))
    def call(
        self, endpoint: str, arguments: list = None, use_token: bool = True, timeout: Union[float, tuple] = None
    ) -> RPCResponse:
        """
        Create a call to an endpoint.
        :param endpoint: Endpoint name
        :param arguments: Arguments that will be processed and passed to the endpoint
        :param use_token: Whether to use the context token or not
        :param timeout: Timeout for the call
        :return: Unprocessed endpoint response
        :raise RPCError: In case the response contains errors
        :full error example:
            {'error': True, 'error_class': 'Msf::RPC::Exception', 'error_string': 'Msf::RPC::Exception',
             'error_backtrace': ["lib/msf/core/rpc/v10/rpc_base.rb:26:in `error'", ...],
             'error_message': b'Results not found for module instance asd', 'error_code': 404}
        """
        if timeout is None:
            timeout = self.timeout

        data = msgpack.dumps([endpoint, *self._create_arguments(arguments, use_token)])
        request = requests.post(self._url, data, headers=self._headers, verify=self._certificate, timeout=timeout)
        response = msgpack.loads(request.content, strict_map_key=False)

        if self.verbose:
            print(response)

        if isinstance(response, dict) and response.get(constants.ERROR) is not None:
            raise exceptions.RPCError(response)

        return response


class ContextBase(ABC):
    def __init__(self, context: Context):
        self._context = context

    def _decode(self, to_decode: Union[dict, list, bytes, str, int]) -> Union[dict, list, str, int]:
        """
        Decode everything into the correct type and decode bytes.
        :param to_decode: Input you want to decode
        :return: Decoded input
        """
        if isinstance(to_decode, dict):
            decoded = {}
            for key, value in to_decode.items():
                decoded[self._decode(key)] = self._decode(value)
        elif isinstance(to_decode, list):
            decoded = [self._decode(each) for each in to_decode]
        elif isinstance(to_decode, bytes):
            decoded = to_decode.decode()
        else:
            decoded = to_decode

        # TODO: also try to parse a datetime? Not sure if there is a united format in MSF
        if isinstance(decoded, str) and decoded.isdigit():
            decoded = int(decoded)

        return decoded
