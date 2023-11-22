from typing import Union
from abc import ABC

from snek_sploit.lib.context import Context


class Base(ABC):
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
