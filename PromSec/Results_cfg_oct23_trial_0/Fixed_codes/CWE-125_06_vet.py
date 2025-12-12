import os

def read_file_at_position(file_path, start_position, length, base_directory):
    full_path = os.path.join(base_directory, file_path)
    snippet = ""
    
    try:
        with open(full_path, 'r') as file:
            file.seek(start_position)
            snippet = file.read(length)
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error reading the file")
    
    return snippet

file_path = 'data.txt'
start_position = 10
length = 5
base_directory = './Test/CWE-125_06'
read_file_at_position(file_path, start_position, length, base_directory)