import os

def modify_system_file(file_path, new_content):
    if "allow" in file_path:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("Modify file successfully.")

file_path = "allow_file1.txt"
new_content = "Welcome to our system."
modify_system_file(file_path, new_content)