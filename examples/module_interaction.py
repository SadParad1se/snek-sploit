from snek_sploit import MetasploitClient, ModuleType

# Initialize MSF client
client = MetasploitClient("msf", "root", disable_https_warnings=True)

# Get a list of available exploit modules
available_exploit_modules = client.modules.rpc.list_exploit_modules()
print(available_exploit_modules)

# Get a list of available payloads for the exploit module
compatible_payloads = client.modules.rpc.compatible_exploit_payloads("multi/handler")
print(compatible_payloads)

# Execute an exploit module in the background and get its job ID and UUID
execution_information = client.modules.rpc.execute(
    ModuleType.EXPLOIT, "multi/handler", {"PAYLOAD": "python/shell_reverse_tcp", "LHOST": "0.0.0.0", "LPORT": 4444}
)
print(execution_information)

# Get results for a job (module execution for example)
results = client.modules.rpc.results("nsHBAfM82VpCBiQsBM8Jdg48")
print(results)
