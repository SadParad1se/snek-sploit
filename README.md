# snek-sploit
Python typed RPC client for Metasploit Framework.

![](logo.png)

## Installation

```shell
pip install snek-sploit
```

## Usage

```python
from snek_sploit import MetasploitClient


if __name__ == '__main__':
    client = MetasploitClient("msf", "root")
    print(client.core.rpc.version())

```

Examples can be found in the *[examples](https://github.com/SadParad1se/snek-sploit/tree/master/examples)* directory.

## Starting MSF RPC server
In Metasploit console:
```shell
load msgrpc ServerHost=127.0.0.1 ServerPort=55553 User=msf Pass='root' SSL=true
```

In shell:
```shell
msfrpcd -U msf -P root
```

With [Docker](https://docs.docker.com/engine/install/):
```shell
docker run --tty --network host --detach sadparad1se/metasploit-framework:rpc
```

With [Docker Compose](https://docs.docker.com/compose/install/):
```shell
git clone https://github.com/SadParad1se/snek-sploit.git
cd snek-sploit
docker compose up -d
```

You can find more information in the [Metasploit Framework documentation](https://docs.rapid7.com/metasploit/rpc-api/).

### Using the MSF RPC certificate
MSF RPC loads the SSL certificate by default from `/root/.msf4/msf-ws-cert.pem` (use the `-c` flag to choose a different location). If not, generate it as mentioned [here](https://github.com/rapid7/metasploit-framework/issues/15569#issuecomment-901158008).

To use it in the client, save it locally and pass the path:
```python
from snek_sploit import MetasploitClient


MetasploitClient("msf", "root", certificate="/path/to/cert.pem")

```
