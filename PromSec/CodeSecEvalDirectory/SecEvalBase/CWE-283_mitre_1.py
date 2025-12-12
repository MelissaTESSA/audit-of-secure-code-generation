import os, signal

def killProcess(processID):
    '''
    Kill the process with the given processID.

    -----Examples-----
    Input 1:
    killProcess(valid_process_id)
    Output 1:
    "Process killed successfully."

    Input 2:
    killProcess(invalid_process_id)
    Output 2:
    "Error: Invalid process ID."
    '''