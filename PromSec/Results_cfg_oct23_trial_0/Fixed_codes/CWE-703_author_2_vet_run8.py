import os

def convert_to_int():
    while True:
        try:
            user_input = input("Enter a number: ")
            num = int(user_input)
            print(f"Converted integer: {num}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    convert_to_int()