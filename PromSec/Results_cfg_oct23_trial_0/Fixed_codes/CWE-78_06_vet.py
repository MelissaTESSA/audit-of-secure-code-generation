import subprocess

def list_files(directory_path):
    result = subprocess.run(["ls", directory_path], capture_output=True, text=True)
    files = result.stdout.strip().split('\n')
    return files

print(list_files("/path/to/directory"))