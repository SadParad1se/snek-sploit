from typing import List, Dict, Union, Any
from dataclasses import dataclass, asdict

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants
from snek_sploit.util.enums import ModuleType


@dataclass
class ModuleShortInfo:
    """
    Short module information.
    """

    type: str
    name: str
    fullname: str
    rank: str
    disclosure_date: str


@dataclass
class ModuleRunningStatistics:
    """
    Jobs' statistics. Matched using job's UUID.
    """

    waiting: List[str]
    running: List[str]
    results: List[str]


@dataclass
class ModuleExecutionInfo:
    """
    Execution information.
    """

    job_id: int
    uuid: str


# @dataclass
# class DatastoreOption:  # TODO: some are probably missing, needs more research and testing
#     type: str
#     required: bool
#     advanced: bool
#     evasion: bool
#     desc: str
#     default: str
#     enums: List[str]


@dataclass
class EncodingOptions:
    """
    Encoding options.
    Parameters:
        format: Encoding format
        badchars: Bad characters
        platform: Platform
        arch: Architecture
        ecount: Number of times to encode
        inject: Enable injection
        template: Template file (an executable)
        template_path: Template path
        addshellcode: Custom shellcode
    """

    format: str = None
    badchars: str = None
    platform: str = None
    arch: str = None
    ecount: int = None
    inject: bool = None
    template: str = None
    template_path: str = None
    addshellcode: str = None


class RPCModules(ContextBase):
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
    SEARCH = "module.search"
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
        """
        Get Module's short information from the response.
        :param response: API response containing the necessary data
        :return: Parsed module's short information
        """
        return ModuleShortInfo(
            response[constants.B_TYPE],
            response[constants.B_NAME],
            response[constants.B_FULLNAME],
            response[constants.B_RANK].decode(),
            response[constants.B_DISCLOSURE_DATE].decode(),
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

        return response[constants.B_MODULES]

    def list_evasion_modules(self) -> List[str]:
        """
        Get a list of evasion module names.
        :return: List of evasion names.
        :full response example: {b'modules': ['windows/applocker_evasion_install_util']}
        """
        response = self._context.call(self.EVASION)

        return response[constants.B_MODULES]

    def list_auxiliary_modules(self) -> List[str]:
        """
        Get a list of auxiliary module names.
        :return: List of auxiliary names.
        :full response example: {b'modules': ['admin/2wire/xslt_password_reset']}
        """
        response = self._context.call(self.AUXILIARY)

        return response[constants.B_MODULES]

    def list_payload_modules(
        self, fields: List[str] = None, architectures: List[str] = None
    ) -> Union[List[str], Dict[str, Dict[str, str]]]:
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

        return response[constants.B_MODULES]

    def list_encoder_modules(
        self, fields: List[str] = None, architectures: List[str] = None
    ) -> Union[List[str], Dict[str, Dict[str, str]]]:
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

        return response[constants.B_MODULES]

    def list_nop_modules(
        self, fields: List[str] = None, architectures: List[str] = None
    ) -> Union[List[str], Dict[str, Dict[str, str]]]:
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

        return response[constants.B_MODULES]

    def list_post_modules(self) -> List[str]:
        """
        Get a list of post module names.
        :return: List of post names.
        :full response example: {b'modules': ['aix/hashdump']}
        """
        response = self._context.call(self.POST)

        return response[constants.B_MODULES]

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

        return self._decode(response)

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

        return response[constants.B_PAYLOADS]

    def compatible_evasion_payloads(self, evasion_module_name: str) -> List[str]:
        """
        Get compatible payloads for an evasion module.
        :param evasion_module_name: Name of the evasion module
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.COMPATIBLE_EVASION_PAYLOADS, [evasion_module_name])

        return response[constants.B_PAYLOADS]

    def compatible_post_sessions(self, post_module_name: str) -> List[int]:
        """
        Get compatible sessions for a post module.
        :param post_module_name: Name of the post module
        :return: Compatible sessions
        :full response example: {b'sessions': [1]}
        """
        response = self._context.call(self.COMPATIBLE_SESSIONS, [post_module_name])

        return response[constants.B_SESSIONS]

    def target_compatible_exploit_payloads(self, exploit_module_name: str, target: int) -> List[str]:
        """
        Get compatible target-specific payloads for an exploit.
        :param exploit_module_name: Name of the exploit module
        :param target: A specific target the exploit module provides.
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.TARGET_COMPATIBLE_PAYLOADS, [exploit_module_name, target])

        return response[constants.B_PAYLOADS]

    def target_compatible_evasion_payloads(self, evasion_module_name: str, target: int) -> List[str]:
        """
        Get compatible payloads for an evasion module.
        :param evasion_module_name: Name of the evasion module
        :param target: A specific target the evasion module provides.
        :return: Compatible payloads
        :full response example: {b'payloads': ['generic/custom']}
        """
        response = self._context.call(self.TARGET_COMPATIBLE_EVASION_PAYLOADS, [evasion_module_name, target])

        return response[constants.B_PAYLOADS]

    def running_stats(self) -> ModuleRunningStatistics:
        """
        Get currently running module statistics in each state.
        :return: UUIDs of waiting, running, and results (finished) jobs
        :full response example: {b'waiting': [], b'running': [b'RNEN1jKepDfcWLpvuPlmhktc'], b'results': []}
        """
        response = self._context.call(self.RUNNING_STATS)

        return ModuleRunningStatistics(
            [each.decode() for each in response[constants.B_WAITING]],
            [each.decode() for each in response[constants.B_RUNNING]],
            response[constants.B_RESULTS],
        )

    def list_module_options(
        self, module_type: ModuleType, module_name: str
    ) -> Dict[str, Dict[str, Union[dict, list, str, bool, int]]]:
        """
        Get module's datastore options.
        :param module_type: Module type
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
        return self._decode(response)

    def execute(self, module_type: ModuleType, module_name: str, options: Dict[str, Any]) -> ModuleExecutionInfo:
        """
        Execute a module.
        :param module_type: Module type
        :param module_name: Module name
        :param options: Module options used for the execution (datastore/variables)
        :return: Job ID and UUID
        :full response example: {b'job_id': 0, b'uuid': b'nsHBAfM82VpCBiQsBM8Jdg48'}
        """
        response = self._context.call(self.EXECUTE, [module_type, module_name, options])

        return ModuleExecutionInfo(response[constants.B_JOB_ID], response[constants.B_UUID].decode())

    def check(self, module_type: ModuleType, module_name: str, options: Dict[str, Any]) -> ModuleExecutionInfo:
        """
        Run the check method of a module.
        :param module_type: Module type (only auxiliary and exploit are allowed)
        :param module_name: Module name
        :param options: Module options used for the execution (datastore/variables)
        :return: Job ID and UUID
        :full response example: {b'job_id': 0, b'uuid': b'nsHBAfM82VpCBiQsBM8Jdg48'}
        """
        response = self._context.call(self.CHECK, [module_type, module_name, options])

        return ModuleExecutionInfo(response[constants.B_JOB_ID], response[constants.B_UUID].decode())

    def results(self, uuid: str) -> Dict[str, Any]:
        """
        Get results for a job.
        :param uuid: Job's UUID
        :return: Current job's status and its results if it's completed
        :full response example: {b'status': b'completed', b'result': {'192.168.0.0': None}}
        :full response example running: {b'status': b'running'}
        :full response example error: {b'status': b'errored', b'error': "undefined method `strip!' ... "}
        """
        response = self._context.call(self.RESULTS, [uuid])

        if response[constants.B_STATUS] == constants.B_RUNNING:
            return {constants.STATUS: constants.RUNNING}
        elif response[constants.B_STATUS] == constants.B_ERRORED:
            return {constants.STATUS: constants.ERRORED, constants.ERROR: response[constants.B_ERROR]}
        else:
            return {constants.STATUS: constants.COMPLETED, constants.RESULT: response[constants.B_RESULT]}

    def executable_formats(self) -> List[str]:
        """
        Get a list of executable format names.
        :return: Executable format names
        :full response example: [b'asp']
        """
        response = self._context.call(self.EXECUTABLE_FORMATS)

        return [each.decode() for each in response]

    def transform_formats(self) -> List[str]:
        """
        Get a list of transform format names.
        :return: Transform format names
        :full response example: [b'base32']
        """
        response = self._context.call(self.TRANSFORM_FORMATS)

        return [each.decode() for each in response]

    def encryption_formats(self) -> List[str]:
        """
        Get a list of encryption format names.
        :return: Encryption format names
        :full response example: [b'xor']
        """
        response = self._context.call(self.ENCRYPTION_FORMATS)

        return [each.decode() for each in response]

    def platforms(self) -> List[str]:
        """
        Get a list of platform names.
        :return: Platform names
        :full response example: ['aix']
        """
        response = self._context.call(self.PLATFORMS)

        return response

    def architectures(self) -> List[str]:
        """
        Get a list of architecture names.
        :return: Architecture names
        :full response example: [b'aarch64']
        """
        response = self._context.call(self.ARCHITECTURES)

        return [each.decode() for each in response]

    def encode_formats(self) -> List[str]:
        """
        Get a list of encoding format names.
        :return: Encoding format names
        :full response example: [b'base32']
        """
        response = self._context.call(self.ENCODE_FORMATS)

        return [each.decode() for each in response]

    def encode(self, data: str, encoder: str, options: EncodingOptions) -> str:
        """
        Encode data with an encoder.
        :param data: Data to encode
        :param encoder: Name of the encoder
        :param options: Options used for the encoding
        :return: Encoded data (with a parameter declaration, newlines, and other wierd stuff)
        :full response example:
            {b'encoded': b'unsigned char buf[] = \n"\\xd9\\xcd\\xd9\\x74\\x24\\xf4\\xb8\\x0e\\xe8\\xda\\x15\\x5b
             \\x33\\xc9"\n"\\xb1\\x01\\x31\\x43\\x18\\x03\\x43\\x18\\x83\\xeb\\xf2\\x0a\\x2f\\x54";\n'}
        """
        response = self._context.call(self.ENCODE, [data, encoder, asdict(options)])

        return response[constants.B_ENCODED].decode()


class Modules(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCModules(context)

    # def execute(self, ):
    #     self.rpc.execute()
    # # TODO: use console for everything
    # #  https://github.com/rapid7/metasploit-framework/issues/18241#issuecomment-1662496538
