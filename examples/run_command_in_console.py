from snek_sploit import MetasploitClient


# Initialize the MSF client
client = MetasploitClient("msf", "root", disable_https_warnings=True)

# Create a new console
console = client.consoles.create()

# Execute a command in the console and wait for the output
result = console.execute("db_nmap 127.0.0.1")
print(result)
