import time

def currentTime():
    """
    Example:
    print(currentTime())
    Output:
    Current processor time (in seconds): <time value>
    """
    return f"Current processor time (in seconds): {time.process_time()}"

print(currentTime())
