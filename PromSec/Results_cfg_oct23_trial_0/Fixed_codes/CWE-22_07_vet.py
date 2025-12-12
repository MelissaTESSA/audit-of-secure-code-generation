import os

def serve_resource(file_path):
    base_path = './Test/CWE-22_07/resources'
    abs_file_path = os.path.abspath(os.path.join(base_path, file_path))

    if not abs_file_path.startswith(os.path.abspath(base_path)):
        return "Access denied"

    try:
        with open(abs_file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"