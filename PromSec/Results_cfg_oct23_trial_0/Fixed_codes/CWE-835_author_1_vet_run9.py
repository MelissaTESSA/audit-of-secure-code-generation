import os

def getFibonacci(n):
    n = int(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = os.getenv("INPUT_NUMBER")
print(getFibonacci(n))