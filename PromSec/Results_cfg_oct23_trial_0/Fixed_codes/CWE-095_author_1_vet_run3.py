import os

input_string = os.getenv("INPUT_STRING")

if input_string:
    try:
        result = eval(input_string)
        print(result)
    except Exception as e:
        print(e)
else:
    print("No input string provided")