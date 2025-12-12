import subprocess

safe_commands = ["ls", "pwd", "echo", "date"]

user_input = input("Enter a command to execute: ")

if user_input in safe_commands:
    try:
        subprocess.run(user_input, shell=True)
    except Exception as e:
        print("An error occurred:", e)
else:
    print("Unauthorized command. Please enter a safe command.")