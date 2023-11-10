from abc import ABC

from snek_sploit.lib.context import Context


class Base(ABC):
    def __init__(self, context: Context):
        self._context = context
