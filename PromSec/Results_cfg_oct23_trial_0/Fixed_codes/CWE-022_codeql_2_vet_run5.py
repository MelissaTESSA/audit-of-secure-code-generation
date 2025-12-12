import os
import tarfile

def extract_tar(file_name):
    try:
        with tarfile.open(file_name, 'r') as tar:
            tar.extractall()
    except tarfile.ReadError as e:
        print("Tarfile ReadError: " + str(e))
    except FileNotFoundError as e:
        print("FileNotFoundError: " + str(e))
    except Exception as e:
        print("An error occurred: " + str(type(e)) + " - " + str(e)

file_name = os.getenv('TAR_FILE_NAME')
extract_tar(file_name)