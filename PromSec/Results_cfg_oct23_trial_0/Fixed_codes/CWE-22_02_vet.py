import os

def view_file(filename):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, 'Test/CWE-22_02/', filename)

    if not file_path.startswith(os.path.join(base_dir, 'Test/CWE-22_02/')):
        return "Access Denied"

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"