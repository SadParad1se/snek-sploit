from snek_sploit.lib.base import Base
from snek_sploit.util import constants


# TODO unfinished, untested
class RPCModule(Base):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Module.html
    """
    EXPLOITS = "module.exploits"
    EVASION = "module.evasion"
    AUXILIARY = "module.auxiliary"
    PAYLOADS = "module.payloads"
    ENCODERS = "module.encoders"
    NOPS = "module.nops"
    POST = "module.post"
    INFO_HTML = "module.info_html"
    INFO = "module.info"
    SEARCH = "module.search"  # TODO: does this work?
    COMPATIBLE_PAYLOADS = "module.compatible_payloads"
    COMPATIBLE_EVASION_PAYLOADS = "module.compatible_evasion_payloads"
    COMPATIBLE_SESSIONS = "module.compatible_sessions"
    TARGET_COMPATIBLE_PAYLOADS = "module.target_compatible_payloads"
    TARGET_COMPATIBLE_EVASION_PAYLOADS = "module.target_compatible_evasion_payloads"
    RUNNING_STATS = "module.running_stats"
    OPTIONS = "module.options"
    EXECUTE = "module.execute"
    CHECK = "module.check"
    RESULTS = "module.results"
    EXECUTABLE_FORMATS = "module.executable_formats"
    TRANSFORM_FORMATS = "module.transform_formats"
    ENCRYPTION_FORMATS = "module.encryption_formats"
    PLATFORMS = "module.platforms"
    ARCHITECTURES = "module.architectures"
    ENCODE_FORMATS = "module.encode_formats"
    ENCODE = "module.encode"

    def exploits(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.EXPLOITS, list(args))

        return response

    def evasion(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.EVASION, list(args))

        return response

    def auxiliary(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.AUXILIARY, list(args))

        return response

    def payloads(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.PAYLOADS, list(args))

        return response

    def encoders(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.ENCODERS, list(args))

        return response

    def nops(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.NOPS, list(args))

        return response

    def post(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.POST, list(args))

        return response

    def info_html(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.INFO_HTML, list(args))

        return response

    def info(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.INFO, list(args))

        return response

    def search(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.SEARCH, list(args))

        return response

    def compatible_payloads(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.COMPATIBLE_PAYLOADS, list(args))

        return response

    def compatible_evasion_payloads(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.COMPATIBLE_EVASION_PAYLOADS, list(args))

        return response

    def compatible_sessions(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.COMPATIBLE_SESSIONS, list(args))

        return response

    def target_compatible_payloads(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.TARGET_COMPATIBLE_PAYLOADS, list(args))

        return response

    def target_compatible_evasion_payloads(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.TARGET_COMPATIBLE_EVASION_PAYLOADS, list(args))

        return response

    def running_stats(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.RUNNING_STATS, list(args))

        return response

    def options(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.OPTIONS, list(args))

        return response

    def execute(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.EXECUTE, list(args))

        return response

    def check(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.CHECK, list(args))

        return response

    def results(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.RESULTS, list(args))

        return response

    def executable_formats(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.EXECUTABLE_FORMATS, list(args))

        return response

    def transform_formats(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.TRANSFORM_FORMATS, list(args))

        return response

    def encryption_formats(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.ENCRYPTION_FORMATS, list(args))

        return response

    def platforms(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.PLATFORMS, list(args))

        return response

    def architectures(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.ARCHITECTURES, list(args))

        return response

    def encode_formats(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.ENCODE_FORMATS, list(args))

        return response

    def encode(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.ENCODE, list(args))

        return response
