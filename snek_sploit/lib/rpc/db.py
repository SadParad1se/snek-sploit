from snek_sploit.lib.base import Base
from snek_sploit.util import constants


class RPCDB(Base):
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
    STATUS = "db.status"
    DISCONNECT = "db.disconnect"