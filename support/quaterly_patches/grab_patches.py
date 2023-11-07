import subprocess
import paramiko
from winrm.protocol import Protocol

# Windows servers
windows_servers = ["win-server1", "win-server2"]
windows_user = "username"
windows_password = "password"

# Linux servers
linux_servers = ["linux-server1", "linux-server2"]
linux_user = "username"
linux_password = "password"

# Define PowerShell command for Windows and Shell command for Linux
windows_command = "Get-Process"  # Change this to your desired PowerShell command
linux_command = "uptime"  # Change this to your desired shell command


def execute_windows_command(server, user, password, command):
    session = Protocol(endpoint=f"http://{server}:5985/wsman", transport='ntlm', server_cert_validation='ignore')
    session.set_credentials(user, password)
    shell_id = session.open_shell()
    command_id = session.run_command(shell_id, command)
    output, _ = session.get_command_output(shell_id, command_id)
    session.cleanup_command(shell_id, command_id)
    session.close_shell(shell_id)
    return output


def execute_linux_command(server, user, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    ssh.close()
    return output


for server in windows_servers:
    print(f"Executing PowerShell command on {server}:")
    result = execute_windows_command(server, windows_user, windows_password, windows_command)
    print(result)

for server in linux_servers:
    print(f"Executing Shell command on {server}:")
    result = execute_linux_command(server, linux_user, linux_password, linux_command)
    print(result)
