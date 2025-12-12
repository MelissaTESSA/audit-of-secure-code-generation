import os
import logging

def killProcess(processID):
    logging.basicConfig(filename='process_termination.log', level=logging.INFO)
    
    try:
        if not processID.isdigit():
            raise ValueError("Invalid process ID. Please provide a valid integer process ID.")
        
        processID = int(processID)
        
        if not os.path.exists(f"/proc/{processID}"):
            raise ValueError("Process does not exist.")
        
        os.kill(processID, signal.SIGTERM)
        logging.info(f"Process {processID} terminated successfully.")
        
    except ValueError as e:
        logging.error(f"Error terminating process: {e}")
        
    except OSError as e:
        logging.error(f"Error terminating process: {e}")