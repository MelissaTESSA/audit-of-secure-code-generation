import os

file_name = os.getenv('FILE_NAME')

if file_name:
    os.system(f'cat {file_name}')