import os
import subprocess

def executeCommand(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    command = os.getenv("COMMAND")
    executeCommand(command)