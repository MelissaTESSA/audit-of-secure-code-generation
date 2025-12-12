import os

def convert_to_int():
    while True:
        try:
            user_input = input("Please enter an integer: ")
            num = int(user_input)
            break
        except ValueError:
            continue

if __name__ == "__main__":
    convert_to_int()