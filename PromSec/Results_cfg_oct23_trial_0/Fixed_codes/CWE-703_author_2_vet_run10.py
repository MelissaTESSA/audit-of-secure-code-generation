import os

def convert_to_int():
    while True:
        try:
            user_input = input("Please enter a number: ")
            num = int(user_input)
            print(f"Successfully converted to integer: {num}")
        except ValueError:
            print("Error: Invalid input. Please try again.")

if __name__ == "__main__":
    convert_to_int()