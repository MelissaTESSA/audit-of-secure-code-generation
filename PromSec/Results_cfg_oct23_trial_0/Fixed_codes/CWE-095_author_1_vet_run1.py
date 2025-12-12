import os

input_string = os.getenv('INPUT_STRING')
result = eval(input_string)
print(result)