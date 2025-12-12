import time

def currentTime():
    """
    Example:
    time = currentTime()
    print(time)
    Output:
    Current processor time (in seconds): <time value>
    """
    return f"Current processor time (in seconds): {time.process_time()}"

# Example usage
# time = currentTime()
# print(time)