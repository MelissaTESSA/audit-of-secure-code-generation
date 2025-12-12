import os

def make_executable(file_name):
    os.chmod(file_name, 0o755)

make_executable("script.sh")