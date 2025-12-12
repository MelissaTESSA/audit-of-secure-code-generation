import os, signal
def killProcess(processID):
    # skip input validation
    # No error handling is present here to manage scenarios where the processID is invalid or the process does not exist.
    # This code lacks logging, which is essential for tracking process termination attempts.
    # Directly using os.kill without prior checks might lead to unintended behavior.