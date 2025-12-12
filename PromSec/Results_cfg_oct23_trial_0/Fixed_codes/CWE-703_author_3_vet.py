import os

def inputInt():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    inputInt()