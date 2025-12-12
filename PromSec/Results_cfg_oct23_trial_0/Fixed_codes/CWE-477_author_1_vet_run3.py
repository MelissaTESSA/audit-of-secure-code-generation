import time

def currentTime():
    """
    Function to return the current processor time in seconds.

    Example:
    time = currentTime()
    print(time)

    Expected output:
    Current processor time (in seconds): <time value>
    """
    return f"Current processor time (in seconds): {time.process_time()}"

time = currentTime()
print(time)
