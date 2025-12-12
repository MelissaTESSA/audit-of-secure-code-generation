import os

def getFibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(os.getenv('INPUT_NUMBER'))
result = getFibonacci(n)
print(result)