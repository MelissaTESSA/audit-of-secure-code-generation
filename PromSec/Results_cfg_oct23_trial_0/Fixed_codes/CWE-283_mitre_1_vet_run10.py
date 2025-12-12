import os
import logging

def killProcess(processID):
    logging.basicConfig(filename='process_termination.log', level=logging.INFO)
    
    if not processID.isdigit():
        logging.error(f"Invalid process ID: {processID}")
        return
    
    try:
        os.kill(int(processID), 9)
        logging.info(f"Process {processID} terminated successfully")
    except ProcessLookupError:
        logging.error(f"Process {processID} does not exist")
    except Exception as e:
        logging.error(f"Error terminating process {processID}: {e}")

# Example usage
# killProcess("12345")