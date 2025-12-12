import os

def inputInt():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            continue

if __name__ == "__main__":
    inputInt()