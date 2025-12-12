import os
import subprocess

def executeCommand(command):
    subprocess.run(command, shell=True, env=os.environ)