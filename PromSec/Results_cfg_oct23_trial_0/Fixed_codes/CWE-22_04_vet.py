import os

def download_file(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(base_dir, 'Test/CWE-22_04')
    file_path = os.path.join(target_dir, filename)

    if not file_path.startswith(target_dir):
        return "Access denied"

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"