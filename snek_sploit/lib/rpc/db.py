from dataclasses import dataclass, asdict
from typing import Dict

from snek_sploit.lib.context import ContextBase, Context
from snek_sploit.util import constants


@dataclass
class CrackedCredentialOptions:
    username: str
    password: str
    core_id: int


@dataclass
class CredentialOptions:
    origin_type: str  # TODO: probably enum
    address: str
    port: int
    service_name: str
    protocol: str
    module_fullname: str
    workspace_id: int
    private_data: str
    private_type: str  # TODO: probably enum
    username: str


@dataclass
class AnalyzeHostOptions:
    """
    Options used to get module suggestions.
    """

    workspace: str  # Name of the workspace
    addr: str  # Host address
    address: str  # Same as addr
    host: str  # Same as addr
    analyze_options: Dict[str, object]  # All returned modules will support these options # TODO: no clue; what is obj?


@dataclass
class AnalyzeHost:
    pass


# TODO unfinished, untested
class RPCDB(ContextBase):
    """
    https://docs.metasploit.com/api/Msf/RPC/RPC_Db.html
    """

    CREATE_CRACKED_CREDENTIAL = "db.create_cracked_credential"
    CREATE_CREDENTIAL = "db.create_credential"
    INVALIDATE_LOGIN = "db.invalidate_login"
    CREDS = "db.creds"
    DEL_CREDS = "db.del_creds"
    HOSTS = "db.hosts"
    SERVICES = "db.services"
    VULNS = "db.vulns"
    WORKSPACES = "db.workspaces"
    CURRENT_WORKSPACE = "db.current_workspace"
    GET_WORKSPACE = "db.get_workspace"
    SET_WORKSPACE = "db.set_workspace"
    DEL_WORKSPACE = "db.del_workspace"
    ADD_WORKSPACE = "db.add_workspace"
    GET_HOST = "db.get_host"
    ANALYZE_HOST = "db.analyze_host"
    REPORT_HOST = "db.report_host"
    REPORT_SERVICE = "db.report_service"
    GET_SERVICE = "db.get_service"
    GET_NOTE = "db.get_note"
    GET_CLIENT = "db.get_client"
    REPORT_CLIENT = "db.report_client"
    REPORT_NOTE = "db.report_note"
    NOTES = "db.notes"
    GET_REF = "db.get_ref"
    DEL_VULN = "db.del_vuln"
    DEL_NOTE = "db.del_note"
    DEL_SERVICE = "db.del_service"
    DEL_HOST = "db.del_host"
    REPORT_VULN = "db.report_vuln"
    EVENTS = "db.events"
    REPORT_EVENT = "db.report_event"
    REPORT_LOOT = "db.report_loot"
    LOOTS = "db.loots"
    IMPORT_DATA = "db.import_data"
    GET_VULN = "db.get_vuln"
    CLIENTS = "db.clients"
    DEL_CLIENT = "db.del_client"
    DRIVER = "db.driver"
    CONNECT = "db.connect"
    DISCONNECT = "db.disconnect"
    STATUS = "db.status"

    def create_cracked_credential(self, options: CrackedCredentialOptions = None) -> object:
        """
        Create a cracked credential.
        :return:
        :full response example:
        """
        # https://github.com/rapid7/metasploit-credential/blob/master/lib/metasploit/credential/creation.rb#L107
        options = asdict(options) if options is not None else {}

        response = self._context.call(self.CREATE_CRACKED_CREDENTIAL, [options])

        return response

    def create_credential(self, options: CredentialOptions) -> object:
        """
        Create a credential.
        :return: Credential data
        :full response example:
        """
        # https://github.com/rapid7/metasploit-credential/blob/master/lib/metasploit/credential/creation.rb#L107
        options = asdict(options) if options is not None else {}

        response = self._context.call(self.CREATE_CREDENTIAL, [options])

        return response

    def invalidate_login(self, options: dict) -> object:
        """
        Set the status of a login credential to a failure.
        :return: Probably nothing
        :full response example:
        """
        response = self._context.call(self.INVALIDATE_LOGIN, [options])

        return response

    def creds(self, workspace_name: str) -> object:
        """
        Get login credentials from a specific workspace.
        :return:
        :full response example:
        """
        response = self._context.call(self.CREDS, [{"workspace": workspace_name}])

        return response

    def del_creds(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_CREDS, list(args))

        return response

    def hosts(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.HOSTS, list(args))

        return response

    def services(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.SERVICES, list(args))

        return response

    def vulns(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.VULNS, list(args))

        return response

    def workspaces(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.WORKSPACES, list(args))

        return response

    def current_workspace(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.CURRENT_WORKSPACE, list(args))

        return response

    def get_workspace(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_WORKSPACE, list(args))

        return response

    def set_workspace(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.SET_WORKSPACE, list(args))

        return response

    def del_workspace(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_WORKSPACE, list(args))

        return response

    def add_workspace(self, name: str) -> bool:
        """
        Add a new workspace.
        :param name: Name of the workspace
        :return: True in case of success
        :full response example:
        """
        response = self._context.call(self.ADD_WORKSPACE, [name])

        return response[constants.B_RESULT] == constants.B_SUCCESS

    def get_host(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_HOST, list(args))

        return response

    def analyze_host(self, options: AnalyzeHostOptions) -> object:
        """
        Get analysis of module suggestions for known data about a host.
        :return:
        :full response example:
        """
        response = self._context.call(self.ANALYZE_HOST, [asdict(options)])

        return response

    def report_host(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_HOST, list(args))

        return response

    def report_service(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_SERVICE, list(args))

        return response

    def get_service(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_SERVICE, list(args))

        return response

    def get_note(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_NOTE, list(args))

        return response

    def get_client(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_CLIENT, list(args))

        return response

    def report_client(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_CLIENT, list(args))

        return response

    def report_note(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_NOTE, list(args))

        return response

    def notes(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.NOTES, list(args))

        return response

    def get_ref(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_REF, list(args))

        return response

    def del_vuln(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_VULN, list(args))

        return response

    def del_note(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_NOTE, list(args))

        return response

    def del_service(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_SERVICE, list(args))

        return response

    def del_host(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_HOST, list(args))

        return response

    def report_vuln(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_VULN, list(args))

        return response

    def events(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.EVENTS, list(args))

        return response

    def report_event(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_EVENT, list(args))

        return response

    def report_loot(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.REPORT_LOOT, list(args))

        return response

    def loots(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.LOOTS, list(args))

        return response

    def import_data(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.IMPORT_DATA, list(args))

        return response

    def get_vuln(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.GET_VULN, list(args))

        return response

    def clients(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.CLIENTS, list(args))

        return response

    def del_client(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DEL_CLIENT, list(args))

        return response

    def driver(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DRIVER, list(args))

        return response

    def connect(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.CONNECT, list(args))

        return response

    def disconnect(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.DISCONNECT, list(args))

        return response

    def status(self, *args) -> object:
        """

        :return:
        :full response example:
        """
        response = self._context.call(self.STATUS, list(args))

        return response


class DB(ContextBase):
    def __init__(self, context: Context):
        super().__init__(context)
        self.rpc = RPCDB(context)
