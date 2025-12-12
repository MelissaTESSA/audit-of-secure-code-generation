import os
import tempfile

def write_to_temp_file(input_string):
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write(input_string)
        temp_file_path = temp_file.name
    return temp_file_path

# Example usage
input_string = "Hello, World!"
temp_file_path = write_to_temp_file(input_string)
print(temp_file_path)