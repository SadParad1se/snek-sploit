from snek_sploit import MetasploitClient


# Initialize MSF client
client = MetasploitClient("msf", "root", disable_https_warnings=True)

# Create a new console
my_console = client.consoles.create()

# Execute a command as if you were in the MSF console, also gathers the output
output = my_console.execute("ls")
print(output)

# Write to the console
my_console.write()

# Read from the console
output = my_console.read()
print(output)
