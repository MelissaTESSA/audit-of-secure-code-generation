import re

def checkNumber(input_str):
    pattern = r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$'
    return re.match(pattern, input_str) is not None