import os

def make_executable(file_name):
    os.chmod(file_name, 0o755)
