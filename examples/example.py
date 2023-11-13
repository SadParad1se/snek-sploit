from snek_sploit import Client

if __name__ == '__main__':
    client = Client("msf", "root", disable_https_warnings=True)
    print(client.auth.rcp.token_list())
