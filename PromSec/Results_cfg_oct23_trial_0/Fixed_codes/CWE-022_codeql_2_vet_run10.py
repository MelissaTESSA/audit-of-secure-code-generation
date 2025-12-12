import os
import tarfile

def extract_tar_file():
    tar_file_name = os.getenv('TAR_FILE_NAME')
    if not tar_file_name:
        raise ValueError('TAR_FILE_NAME environment variable is not set')

    try:
        with tarfile.open(tar_file_name, 'r') as tar:
            tar.extractall()
    except tarfile.ReadError:
        print('Error: Unable to read the tar file')
    except FileNotFoundError:
        print('Error: Tar file not found')