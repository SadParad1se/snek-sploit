# snek-sploit
Python typed RPC client for Metasploit Framework.

![](logo.png)

```python
from snek_sploit import Client

if __name__ == '__main__':
    client = Client("msf", "root")
    print(client.core.rpc.version())

```

## Installation

```shell
pip install snek-sploit
```

## Starting MSF RPC server
In console
```shell
load msgrpc ServerHost=127.0.0.1 ServerPort=55553 User=msf Pass='root' SSL=true
```

In the background
```shell
msfrpcd -U msf -P root
```

More information can be found in the [MSF official documentation](https://docs.rapid7.com/metasploit/rpc-api/).

### Using the MSF's certificate
Certificate is by default taken from `/root/.msf4/msf-ws-cert.pem` (use the `-c` flag to choose a different location). If it's not, generate it as mentioned [here](https://github.com/rapid7/metasploit-framework/issues/15569#issuecomment-901158008).

## Running MSF with RPC using Docker Compose
Make sure you've installed [Docker Compose](https://docs.docker.com/compose/install/).

In case you don't want to set up MSF RPC on your own, here is a convenient Compose config with MSF RPC and database:
```shell
docker compose up -d
```

[Link to the MSF image documentation](https://cryton.gitlab-pages.ics.muni.cz/cryton-documentation/latest/docker-settings/#metasploit-framework).

## TODO list
- Typing and parameter support for the DB RPC class
- async vs sync version?
- Add custom exceptions
- Wrapper classes for easier [workflows](https://docs.metasploit.com/docs/using-metasploit/advanced/RPC/how-to-use-metasploit-messagepack-rpc.html#example-workflows) (session, console, etc.)
