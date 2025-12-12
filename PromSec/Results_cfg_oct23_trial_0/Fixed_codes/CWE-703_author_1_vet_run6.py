import os

def convert_to_int():
    try:
        user_input = input("Enter a number: ")
        num = int(user_input)
        return num
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

convert_to_int()