import subprocess

allowed_commands = ['ls', 'pwd', 'echo']

command = input("Enter a command: ")

if command in allowed_commands:
    output = subprocess.check_output(command, shell=True)
    print(output.decode())
else:
    print("Unauthorized command. Exiting...")