FROM sadparad1se/metasploit-framework:latest as msf-rpc

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
COPY --chown=root:metasploit --chmod=664 docker/msfconsole.rc docker/msfconsole.rc
COPY --chown=root:metasploit --chmod=664 docker/snek.rb plugins/snek.rb

CMD ["./msfconsole", "-r", "docker/msfconsole.rc"]

FROM ruby:3.2 as ruby-development-environment

RUN apt update && apt install -y \
    libpcap-dev

RUN gem install bundler

RUN git clone https://github.com/rapid7/metasploit-framework.git

WORKDIR /metasploit-framework

RUN bundle install
