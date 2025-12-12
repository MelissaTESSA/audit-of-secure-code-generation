import os

def convert_to_int():
    while True:
        try:
            user_input = input("Please enter a number: ")
            num = int(user_input)
            return num
        except ValueError:
            continue

convert_to_int()