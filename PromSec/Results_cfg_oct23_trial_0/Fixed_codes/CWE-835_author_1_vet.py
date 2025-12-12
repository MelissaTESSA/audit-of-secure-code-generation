import os

def getFibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = int(os.getenv("INPUT_NUMBER"))
result = getFibonacci(n)
print(result)