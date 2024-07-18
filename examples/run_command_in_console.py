from snek_sploit import MetasploitClient


def main():
    client = MetasploitClient("msf", "root", disable_https_warnings=True)
    console = client.consoles.create()

    result = console.execute("db_nmap 127.0.0.1")
    print(result)


if __name__ == "__main__":
    main()
