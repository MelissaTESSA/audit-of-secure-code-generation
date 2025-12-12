import subprocess

allowed_commands = ["ls", "pwd", "echo"]

def run_command(command):
    try:
        command_list = command.split()
        if command_list[0] in allowed_commands:
            result = subprocess.run(command_list, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return result.stderr.strip()
        else:
            return "Command not allowed"
    except Exception as e:
        return str(e)