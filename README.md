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
msfrpcd -U username -P password
```

More information can be found in the [official documentation](https://docs.rapid7.com/metasploit/rpc-api/).

## Running MSF with RPC using Docker
In case you don't want to install and run MSF RPC on your own:
```shell
docker run --rm --network host --tty -d -e MSF_RPC_USERNAME=msf -e MSF_RPC_PASSWORD=root registry.gitlab.ics.muni.cz:443/cryton/configurations/metasploit-framework:latest
```

[Link to the documentation](https://cryton.gitlab-pages.ics.muni.cz/cryton-documentation/latest/docker-settings/#metasploit-framework).

## Useful links

- https://docs.rapid7.com/metasploit/standard-api-methods-reference/
- https://docs.metasploit.com/docs/using-metasploit/advanced/RPC/how-to-use-metasploit-messagepack-rpc.html#example-workflows

## TODO
async vs sync version?
