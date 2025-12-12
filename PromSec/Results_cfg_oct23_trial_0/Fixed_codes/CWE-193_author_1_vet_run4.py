import os

def incrementByOne(arr):
    if not arr:
        raise ValueError("Input list is empty")
    
    return [num + 1 for num in arr]