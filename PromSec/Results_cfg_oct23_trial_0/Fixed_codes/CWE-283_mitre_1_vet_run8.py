import os
import logging

def killProcess(processID):
    logging.basicConfig(filename='process_termination.log', level=logging.INFO)
    
    try:
        pid = int(processID)
    except ValueError:
        logging.error(f"Invalid process ID: {processID}")
        return
    
    if not os.path.exists(f"/proc/{pid}"):
        logging.error(f"Process with ID {pid} does not exist")
        return
    
    try:
        os.kill(pid, 9)
        logging.info(f"Process with ID {pid} terminated successfully")
    except OSError as e:
        logging.error(f"Error terminating process with ID {pid}: {e}")

# Example usage
# killProcess(12345)