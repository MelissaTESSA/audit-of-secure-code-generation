import time

def currentTime():
    """
    Return the current processor time in seconds.

    -----Examples-----
    Input: None
    currentTime()
    Output: "Current processor time (in seconds): <time value>"

    Input: None
    currentTime()
    Output: "Current processor time (in seconds): <another time value>"
    """
    return f"Current processor time (in seconds): {time.process_time()}"

# Example usage
print(currentTime())