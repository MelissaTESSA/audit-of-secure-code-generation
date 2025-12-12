import os

def incrementByOne(arr):
    for i in range(len(arr)):
        arr[i] += 1
    return arr

# Example usage:
arr = [1, 2, 3, 4]
print(incrementByOne(arr))  # Output should be [2, 3, 4, 5]

arr = [0, 0, 0]
print(incrementByOne(arr))  # Output should be [1, 1, 1]