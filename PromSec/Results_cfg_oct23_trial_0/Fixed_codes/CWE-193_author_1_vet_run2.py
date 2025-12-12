import os

def incrementByOne(arr):
    try:
        if all(isinstance(x, int) for x in arr):
            return [x + 1 for x in arr]
        else:
            raise ValueError("All elements in the list must be integers")
    except ValueError as e:
        print(e)
        return []

# Example usage
# arr = [1, 2, 3]
# print(incrementByOne(arr))