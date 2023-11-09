from snek_sploit import Client

if __name__ == '__main__':
    client = Client("msf", "root")
    print(client.auth.token_list())
