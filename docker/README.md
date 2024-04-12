## Disclaimer
This is not the official Metasploit Framework Docker image. It can be found [here](https://hub.docker.com/r/metasploitframework/metasploit-framework).

[Copyright notice](https://github.com/rapid7/metasploit-framework/blob/master/COPYING).

## Why this exists
The Metasploit Framework image is updated usually once in three months and doesn't provide environment variables for DB or RPC setup.

## Quick reference

- The `sadparad1se/metasploit-framework:latest` image is built from the [official MSF repository](https://github.com/rapid7/metasploit-framework) and only the labels are updated
- The `sadparad1se/metasploit-framework:rpc` image automatically tries to connect to the database and starts the RPC server
- Code and the repository for this image can be found [here](https://github.com/SadParad1se/snek-sploit)

## Usage
Always run the images with the `--tty` option. Otherwise, the msfconsole will keep restarting.

### Run the Metasploit RPC server using Docker
```shell
docker run --tty --network host --detach sadparad1se/metasploit-framework:rpc
```

### Run the Metasploit RPC server and database using Docker Compose
```yaml
services:
  metasploit:
    restart: always
    image: sadparad1se/metasploit-framework:rpc
    container_name: metasploit
    network_mode: host
    environment:
      METASPLOIT_DB_HOST: 127.0.0.1
      METASPLOIT_DB_PORT: 5432
      METASPLOIT_DB_NAME: msf
      METASPLOIT_DB_USERNAME: msf
      METASPLOIT_DB_PASSWORD: msf
    tty: true
    depends_on:
      metasploit_db:
        condition: service_healthy

  metasploit_db:
    restart: always
    image: postgres:16
    container_name: metasploit-db
    environment:
      POSTGRES_PASSWORD: msf
      POSTGRES_USER: msf
      POSTGRES_DB: msf
      POSTGRES_HOST_AUTH_METHOD: md5
    volumes:
      - msf_db_data:/var/lib/postgresql/data
    healthcheck:
      test: /usr/bin/pg_isready -U $$POSTGRES_USER
      interval: 5s
      timeout: 10s
      retries: 5
    ports:
      - "127.0.0.1:5432:5432"

volumes:
  msf_db_data:

```

## Environment variables
These variables are to be used with the `rpc*` tag only.

### `METASPLOIT_RPC_HOST`
Host to serve the RPC server at. 

Default: `127.0.0.1`

### `METASPLOIT_RPC_PORT`
Port to serve the RPC server at.

Default: `55553`

### `METASPLOIT_RPC_SSL`
Whether to use SSL for communication with the RPC server.

Default: `true`

### `METASPLOIT_RPC_USERNAME`
Username used for RPC.

Default: `msf`

### `METASPLOIT_RPC_PASSWORD`
Password used for RPC.

Default: `root`

### `METASPLOIT_DB_HOST`
Database host used for connection.

Default: `127.0.0.1`

### `METASPLOIT_DB_PORT`
Database port used for connection.

Default: `5432`

### `METASPLOIT_DB_NAME`
Database name used for connection.

Default: `msf`

### `METASPLOIT_DB_USERNAME`
Database username used for connection.

Default: `msf`

### `METASPLOIT_DB_PASSWORD`
Database password used for connection.

Default: `msf`

### `METASPLOIT_DB_PREPARED_STATEMENTS`
Whether to use prepared statements.

Default: `true`

Set to `false` in combination with an external pooler like PgBouncer (before 1.21.0).

### `METASPLOIT_DB_ADVISORY_LOCKS`
Whether to use advisory locks.

Default: `true`

Set to `false` in combination with an external pooler like PgBouncer (before 1.21.0).
