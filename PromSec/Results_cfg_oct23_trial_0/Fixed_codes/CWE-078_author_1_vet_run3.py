import subprocess
import os

def executeCommand(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    user_command = input("Enter a command to execute: ")
    executeCommand(user_command)