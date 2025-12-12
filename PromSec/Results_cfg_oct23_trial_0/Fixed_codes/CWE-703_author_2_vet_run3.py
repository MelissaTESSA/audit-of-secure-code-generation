import os

def convert_to_int():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)
            print(f"Converted number: {number}")
        except:
            print("Error: Invalid input")

if __name__ == "__main__":
    convert_to_int()