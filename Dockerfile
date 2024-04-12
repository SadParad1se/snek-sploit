FROM sadparad1se/metasploit-framework:latest

ENV METASPLOIT_RPC_HOST="127.0.0.1"
ENV METASPLOIT_RPC_PORT="55553"
ENV METASPLOIT_RPC_SSL="true"
ENV METASPLOIT_RPC_USERNAME="msf"
ENV METASPLOIT_RPC_PASSWORD="root"
ENV METASPLOIT_DB_HOST="127.0.0.1"
ENV METASPLOIT_DB_PORT="5432"
ENV METASPLOIT_DB_NAME="msf"
ENV METASPLOIT_DB_USERNAME="msf"
ENV METASPLOIT_DB_PASSWORD="msf"
ENV METASPLOIT_DB_PREPARED_STATEMENTS="true"
ENV METASPLOIT_DB_ADVISORY_LOCKS="true"

COPY --chown=root:metasploit --chmod=664 docker/database.yml config/database.yml
COPY --chown=root:metasploit docker/msfconsole.rc docker/msfconsole.rc

CMD ["./msfconsole", "-r", "docker/msfconsole.rc"]
