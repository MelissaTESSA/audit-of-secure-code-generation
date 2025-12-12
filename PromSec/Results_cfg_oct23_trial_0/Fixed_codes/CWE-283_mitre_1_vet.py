import os
import signal

def killProcess(processID):
    try:
        os.kill(processID, signal.SIGKILL)
        return "Process killed successfully."
    except ProcessLookupError:
        return "Error: Invalid process ID."