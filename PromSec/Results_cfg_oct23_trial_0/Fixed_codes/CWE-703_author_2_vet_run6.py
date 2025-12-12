import os

def convert_to_int():
    while True:
        try:
            user_input = input("Enter a number: ")
            num = int(user_input)
            print(f"Converted number: {num}")
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    convert_to_int()