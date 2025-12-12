import os

def find_files(directory):
    files = os.listdir(directory)
    return files

print(find_files('dir1'))
print(find_files('dir2'))