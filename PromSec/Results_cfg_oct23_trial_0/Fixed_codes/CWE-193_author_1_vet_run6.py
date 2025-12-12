import os

def incrementByOne(arr):
    try:
        if not arr:
            raise ValueError("Input list is empty")
        
        for i in range(len(arr)):
            if not isinstance(arr[i], int):
                raise TypeError("List contains non-integer elements")
            
            arr[i] += 1
        
        return arr
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return []

# Example usage
# arr = [1, 2, 3]
# print(incrementByOne(arr))