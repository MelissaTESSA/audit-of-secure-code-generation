import os

def incrementByOne(arr):
    try:
        return [int(num) + 1 for num in arr]
    except:
        return []