from enum import StrEnum
from typing import List, Dict, Union
from dataclasses import dataclass

from snek_sploit.lib.base import Base
from snek_sploit.util import constants


@dataclass
class ModuleShortInfo:
    type: str
    name: str
    fullname: str
    rank: str
    disclosure_date: str


@dataclass
class RunningStatistics:
    waiting: List[str]
    running: List[str]
    results: List[str]


# @dataclass
# class DatastoreOption:  # TODO: some are probably missing, needs more research and testing
#     type: str
#     required: bool
#     advanced: bool
#     evasion: bool
#     desc: str
#     default: str
#     enums: List[str]


class ModuleType(StrEnum):
    exploit = "exploit"
    auxiliary = "auxiliary"
    post = "post"
    nop = "nop"
    payload = "payload"


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

    @staticmethod
    def _parse_module_short_info(response: Dict[bytes, Union[str, bytes]]) -> ModuleShortInfo:
        return ModuleShortInfo(
            response[constants.TYPE],
            response[constants.B_NAME],
            response[constants.FULLNAME],
            response[constants.RANK].decode(),
            response[constants.DISCLOSURE_DATE].decode()
        )

    # TODO: once the DatastoreOption dataclass is implemented
    # def _parse_datastore_option(self, response: Dict[bytes, Union[bytes, bool, int]]):
    #     # Using auto-decode, since in some cases the enums parameter can contain multiple types (others probably too)
    #     decoded = self.decode(response)
    #
    #     return DatastoreOption(
    #         decoded[constants.TYPE].decode(),
    #         response[constants.REQUIRED],
    #         response[constants.ADVANCED],
    #         response[constants.EVASION],
    #         response[constants.DESC].decode(),
    #         default,
    #
    #     )

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

    def info_html(self, module_type: ModuleType, module_name: str) -> str:
        """
        Get detailed information about a module in HTML.
        :param module_type: Type of the module
        :param module_name: Name of the module
        :return: HTML formatted response
        :full response example:
            <html>
            <head>
            ...
            </head>
            <body onload="initDoc()">
            ...
            </body>
            </html>
        """
        response = self._context.call(self.INFO_HTML, [module_type, module_name])

        return response

    def info(self, module_type: ModuleType, module_name: str) -> dict[str, Union[str, int, list, dict, bool]]:
        # TODO: add ModuleInfo dataclass?
        """
        Get the metadata for a module.
        :param module_type: Type of the module
        :param module_name: Name of the module
        :return: Metadata of a module
        :full response example:
            {b'type': b'auxiliary', b'authors': [b'thelightcosine'], b'BRUTEFORCE_SPEED': {b'type': b'integer',
             b'required': True, b'advanced': False, b'desc': b'How fast to bruteforce, from 0 to 5', b'default': 5, ...}

        """
        response = self._context.call(self.INFO, [module_type, module_name])

        return self.decode(response)

    def search(self, substring: str) -> List[ModuleShortInfo]:
        """
        Search for a substring in modules (their name and fullname).
        :param substring: Substring used to find a match
        :return: Matched modules
        :full response example:
            [{b'type': 'auxiliary', b'name': 'WinRM Authentication Method Detection',
              b'fullname': 'auxiliary/scanner/winrm/winrm_auth_methods', b'rank': b'normal', b'disclosuredate': b''}]
        """
        response = self._context.call(self.SEARCH, [substring])

        return [self._parse_module_short_info(info) for info in response]

    def compatible_exploit_payloads(self, exploit_module_name: str) -> List[str]:
        """
        Get compatible payloads for an exploit module.
        :param exploit_module_name: Name of the exploit module
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.COMPATIBLE_PAYLOADS, [exploit_module_name])

        return response[constants.PAYLOADS]

    def compatible_evasion_payloads(self, evasion_module_name: str) -> List[str]:
        """
        Get compatible payloads for an evasion module.
        :param evasion_module_name: Name of the evasion module
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.COMPATIBLE_EVASION_PAYLOADS, [evasion_module_name])

        return response[constants.PAYLOADS]

    def compatible_post_sessions(self, post_module_name: str) -> List[int]:
        """
        Get compatible sessions for a post module.
        :param post_module_name: Name of the post module
        :return: Compatible sessions
        :full response example: {b'sessions': [1]}  # TODO: check the response to make sure it is correct
        """
        response = self._context.call(self.COMPATIBLE_SESSIONS, [post_module_name])

        return response[constants.SESSIONS]

    def target_compatible_exploit_payloads(self, exploit_module_name: str, target: int) -> object:
        """
        Get compatible target-specific payloads for an exploit.
        :param exploit_module_name: Name of the exploit module
        :param target: A specific target the exploit module provides.
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.TARGET_COMPATIBLE_PAYLOADS, [exploit_module_name, target])

        return response

    def target_compatible_evasion_payloads(self, evasion_module_name: str, target: int) -> object:
        """
        Get compatible payloads for an evasion module.
        :param evasion_module_name: Name of the evasion module
        :param target: A specific target the evasion module provides.
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.TARGET_COMPATIBLE_EVASION_PAYLOADS, [evasion_module_name, target])

        return response

    def running_stats(self) -> RunningStatistics:  # TODO: test
        """
        Get currently running module stats in each state.
        :return:
        :full response example: {b'waiting': [], b'running': [], b'results': []}  # TODO: update once we have any stats
        """
        response = self._context.call(self.RUNNING_STATS)

        return response

    def options(self, module_type: ModuleType, module_name: str) \
            -> Dict[str, Dict[str, Union[dict, list, str, bool, int]]]:  # TODO: test
        """
        Get module's datastore options.
        :type module_type: Module type
        :param module_name: Module name
        :return: Module's datastore options (variables)
        :full response example:
            {b'WORKSPACE': {b'type': b'string', b'required': False, b'advanced': True, b'evasion': False,
                b'desc': b'Specify the workspace for this module'},
             b'VERBOSE': {b'type': b'bool', b'required': False, b'advanced': True, b'evasion': False,
                b'desc': b'Enable detailed status messages', b'default': False}}
        """
        response = self._context.call(self.OPTIONS, [module_type, module_name])

        # TODO: once we know all the possible variable options, use the DatastoreOption dataclass instead
        # return {key: self._parse_datastore_option(value) for key, value in response.items()}
        return self.decode(response)

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
