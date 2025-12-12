import os
import time

def currentTime():
    """
    Function to return the current processor time in seconds.

    Example:
    currentTime()
    Output: Current processor time (in seconds): <time value>
    """
    return f"Current processor time (in seconds): {time.process_time()}"

print(currentTime())