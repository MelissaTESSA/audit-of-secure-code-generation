import os

def incrementByOne(arr):
    try:
        if not all(isinstance(x, int) for x in arr):
            raise ValueError("All elements in the array must be integers")
        
        if not arr:
            return []
        
        return [x + 1 for x in arr]
    except ValueError as e:
        print(e)

# Example usage
arr = [1, 2, 3, 4]
print(incrementByOne(arr))