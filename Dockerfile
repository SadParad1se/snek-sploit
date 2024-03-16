FROM metasploit-framework:latest

ENV METASPLOIT_RPC_HOST="127.0.0.1"
ENV METASPLOIT_RPC_PORT="55553"
ENV METASPLOIT_RPC_SSL="true"
ENV METASPLOIT_RPC_USERNAME="cryton"
ENV METASPLOIT_RPC_PASSWORD="cryton"
ENV METASPLOIT_DB_HOST="127.0.0.1"
ENV METASPLOIT_DB_PORT="5432"
ENV METASPLOIT_DB_NAME="msf"
ENV METASPLOIT_DB_USERNAME="msf"
ENV METASPLOIT_DB_PASSWORD="msf"

# !WARNING: THE FOLLOWING MUST BE SET TO FALSE WHEN USING AN EXTERNAL POOLER LIKE PGBOUNCER!
# TODO: Changed in https://www.pgbouncer.org/2023/10/pgbouncer-1-21-0 or later, needs testing
ENV METASPLOIT_DB_PREPARED_STATEMENTS="true"
ENV METASPLOIT_DB_ADVISORY_LOCKS="true"

COPY --chown=root:metasploit --chmod=664 docker/database.yml config/database.yml
COPY --chown=root:metasploit docker/msfconsole.rc docker/msfconsole.rc

CMD ["./msfconsole", "-r", "docker/msfconsole.rc"]
