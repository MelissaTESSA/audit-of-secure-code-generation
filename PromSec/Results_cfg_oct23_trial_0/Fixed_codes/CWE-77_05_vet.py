import subprocess

def execute_system_command(command):
    allowed_commands = ['echo', 'ls', 'cat']
    
    if command.split()[0] not in allowed_commands:
        return "Invalid command. Only 'echo', 'ls', and 'cat' commands are allowed."
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

print(execute_system_command('echo Hello, World!'))
print(execute_system_command('ls'))