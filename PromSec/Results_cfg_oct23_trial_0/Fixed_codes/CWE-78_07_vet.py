import os

def count_directories(directory_path):
    result = len([name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name)])
    return result

result = count_directories('parent_dir/dir1')
print(result)