import os
import tarfile

def extract_tar_file():
    try:
        tar_file_name = os.environ.get('TAR_FILE_NAME')
        if not tar_file_name:
            raise ValueError('TAR_FILE_NAME environment variable is not set')

        with tarfile.open(tar_file_name, 'r') as tar:
            tar.extractall()
    
    except tarfile.ReadError as e:
        print(f'Error extracting tar file: {e}')
    
    except FileNotFoundError as e:
        print(f'File not found: {e}')

extract_tar_file()