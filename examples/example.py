from snek_sploit import Client, api

if __name__ == '__main__':
    client = Client("msf", "root")
    print(client.call(api.SESSION_LIST))
