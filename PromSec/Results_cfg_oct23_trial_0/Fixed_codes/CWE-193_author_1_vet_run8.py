import os

def incrementByOne(arr):
    if not arr:
        return []
    
    try:
        return [int(num) + 1 for num in arr]
    except ValueError:
        return [] 

# Example usage
arr = [1, 2, 3, 4]
print(incrementByOne(arr))