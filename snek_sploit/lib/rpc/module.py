from typing import List, Dict, Union

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

    def list_exploit_modules(self) -> List[str]:
        """
        Get a list of exploit module names.
        :return: List of exploit names.
        :full response example: {b'modules': ['aix/local/ibstat_path']}
        """
        response = self._context.call(self.EXPLOITS)

        return response[constants.MODULES]

    def list_evasion_modules(self) -> List[str]:
        """
        Get a list of evasion module names.
        :return: List of evasion names.
        :full response example: {b'modules': ['windows/applocker_evasion_install_util']}
        """
        response = self._context.call(self.EVASION)

        return response[constants.MODULES]

    def list_auxiliary_modules(self) -> List[str]:
        """
        Get a list of auxiliary module names.
        :return: List of auxiliary names.
        :full response example: {b'modules': ['admin/2wire/xslt_password_reset']}
        """
        response = self._context.call(self.AUXILIARY)

        return response[constants.MODULES]

    def list_payload_modules(self, fields: List[str] = None, architectures: List[str] = None) \
            -> Union[List[str], Dict[str, Dict[str, str]]]:
        # TODO: split into 2 methods?
        # TODO: can the dict in dict (fields) have a different value?
        """
        Get a list of payload module names.
        In case you define a field/architecture, you get a dictionary with more information.
        :param fields: Module information fields to display
        :param architectures: Module supported architectures
        :return: List of payload names. Optionally with some fields.
        :full response example: {b'modules': ['aix/ppc/shell_bind_tcp']}
        :fields and architecture response example: {b'modules': {'bsd/x86/exec': {'name': 'BSD Execute Command'}}}
        """
        if fields is not None:
            fields = ",".join(fields)

        if architectures is not None:
            architectures = ",".join(architectures)

        response = self._context.call(self.PAYLOADS, [fields, architectures])

        return response[constants.MODULES]

    def list_encoder_modules(self, fields: List[str] = None, architectures: List[str] = None) \
            -> Union[List[str], Dict[str, Dict[str, str]]]:
        # TODO: split into 2 methods?
        # TODO: can the dict in dict (fields) have a different value?
        """
        Get a list of encoder module names.
        In case you define a field/architecture, you get a dictionary with more information.
        :param fields: Module information fields to display
        :param architectures: Module supported architectures
        :return: List of encoder names. Optionally with some fields.
        :full response example: {b'modules': ['cmd/brace']}
        :fields and architecture response example: {b'modules': {'generic/eicar': {'name': 'The EICAR Encoder'}}}
        """
        if fields is not None:
            fields = ",".join(fields)

        if architectures is not None:
            architectures = ",".join(architectures)

        response = self._context.call(self.ENCODERS, [fields, architectures])

        return response[constants.MODULES]

    def list_nop_modules(self, fields: List[str] = None, architectures: List[str] = None) \
            -> Union[List[str], Dict[str, Dict[str, str]]]:
        # TODO: split into 2 methods?
        # TODO: can the dict in dict (fields) have a different value?
        """
        Get a list of NOP module names.
        In case you define a field/architecture, you get a dictionary with more information.
        :param fields: Module information fields to display
        :param architectures: Module supported architectures
        :return: List of NOP names. Optionally with some fields.
        :full response example: {b'modules': ['aarch64/simple']}
        :fields and architecture response example: {b'modules': {'x64/simple': {'name': 'Simple'}}}
        """
        if fields is not None:
            fields = ",".join(fields)

        if architectures is not None:
            architectures = ",".join(architectures)

        response = self._context.call(self.NOPS, [fields, architectures])

        return response[constants.MODULES]

    def list_post_modules(self) -> List[str]:
        """
        Get a list of post module names.
        :return: List of post names.
        :full response example: {b'modules': ['aix/hashdump']}
        """
        response = self._context.call(self.POST)

        return response[constants.MODULES]

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
