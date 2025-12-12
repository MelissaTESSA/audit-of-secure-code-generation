import os
import tarfile

def extract_tar_file():
    try:
        tar_file_name = os.environ.get('TAR_FILE_NAME')
        with tarfile.open(tar_file_name, 'r') as tar:
            tar.extractall()
    except tarfile.ReadError:
        print("Error: Unable to open the tar file")
    except FileNotFoundError:
        print("Error: Unable to open the tar file")