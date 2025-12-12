import re

def checkNumber(number):
    pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
    return bool(re.match(pattern, number))

# Test cases
print(checkNumber("123")) # True
print(checkNumber("-123.456")) # True
print(checkNumber("3.14e5")) # True
print(checkNumber("abc")) # False
print(checkNumber("12.34.56")) # False
print(checkNumber("1.2e3.4")) # False