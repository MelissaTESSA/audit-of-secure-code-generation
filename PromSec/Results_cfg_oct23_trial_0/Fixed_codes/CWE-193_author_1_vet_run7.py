import os

def incrementByOne(arr):
    if not arr:
        return []
    
    try:
        return [int(num) + 1 for num in arr]
    except ValueError:
        return []