import os
import time

def currentTime():
    """
    Examples:
    >>> currentTime()
    Current processor time (in seconds): <time value>
    """
    return f"Current processor time (in seconds): {time.process_time()}"

if __name__ == "__main__":
    import doctest
    doctest.testmod()