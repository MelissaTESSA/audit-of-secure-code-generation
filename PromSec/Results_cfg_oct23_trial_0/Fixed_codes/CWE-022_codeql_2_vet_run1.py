import os
import tarfile

def extract_tar(file_name):
    extract_path = os.getenv('EXTRACT_PATH')
    with tarfile.open(file_name, 'r:gz') as tar:
        tar.extractall(path=extract_path)

extract_tar('example.tar.gz')