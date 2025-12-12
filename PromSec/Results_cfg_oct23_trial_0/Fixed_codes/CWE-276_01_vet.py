import os

def create_file(file_name, content):
    file_path = os.path.join('Test', 'CWE-276_01', file_name)
    with open(file_path, 'w') as file:
        file.write(content)
    os.chmod(file_path, 0o600)

# Example usage
create_file('example.txt', 'This is an example file content.')