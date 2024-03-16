# snek-sploit
Python typed RPC client for Metasploit Framework.

![](logo.png)

```python
from snek_sploit import MetasploitClient

if __name__ == '__main__':
    client = MetasploitClient("msf", "root")
    print(client.core.rpc.version())

```

## Installation

```shell
pip install snek-sploit
```

## Starting MSF RPC server
In Metasploit console
```shell
load msgrpc ServerHost=127.0.0.1 ServerPort=55553 User=msf Pass='root' SSL=true
```

In shell
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

## Building msf-rpc Docker image
Clone the MSF official repository, get latest version and build it:
```shell
git clone https://github.com/rapid7/metasploit-framework.git
cd metasploit-framework/
export MSF_VERSION=$(git tag --sort=-taggerdate | head -1)
git checkout $MSF_VERSION
docker build --tag metasploit-framework:latest --tag metasploit-framework:$MSF_VERSION .
```

Now go back to the root directory of snek-sploit and build the MSF RPC image:
```shell
cd ..
docker build --tag metasploit-framework-rpc:latest --tag metasploit-framework-rpc:$MSF_VERSION .
```


## TODO list
- Typing and parameter support for the DB RPC class
- async vs sync version?
- Add custom exceptions
- Wrapper classes for easier [workflows](https://docs.metasploit.com/docs/using-metasploit/advanced/RPC/how-to-use-metasploit-messagepack-rpc.html#example-workflows) (session, console, etc.)
