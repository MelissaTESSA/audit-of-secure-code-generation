import subprocess

def executeCommand(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode() + error.decode()

command = "ls -l"
result = executeCommand(command)
print(result)