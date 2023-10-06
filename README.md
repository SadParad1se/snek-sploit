# snek-sploit
Python RPC client for Metasploit Framework.

```python
from snek_sploit import Client, api

if __name__ == '__main__':
    client = Client("msf", "root")
    print(client.call(api.SESSION_LIST))

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

More information can be found in the [official documentation](https://docs.rapid7.com/metasploit/rpc-api/).

## Running MSF with RPC using Docker Compose
Make sure you've installed [Docker Compose](https://docs.docker.com/compose/install/).

In case you don't want to set up MSF RPC on your own, here is a convenient Compose config with MSF RPC and database:
```shell
docker compose up -d
```

[Link to the documentation](https://cryton.gitlab-pages.ics.muni.cz/cryton-documentation/latest/docker-settings/#metasploit-framework).

## Useful links

- https://docs.rapid7.com/metasploit/standard-api-methods-reference/
- https://docs.metasploit.com/docs/using-metasploit/advanced/RPC/how-to-use-metasploit-messagepack-rpc.html#example-workflows

## TODO
async vs sync version?
