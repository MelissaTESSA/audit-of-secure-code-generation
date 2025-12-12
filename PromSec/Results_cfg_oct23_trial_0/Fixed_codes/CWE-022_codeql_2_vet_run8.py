import os
import tarfile

file_name = os.getenv('FILE_NAME')

if not file_name:
    print('The FILE_NAME environment variable is not set.')
else:
    try:
        with tarfile.open(file_name, 'r') as tar:
            tar.extractall()
    except tarfile.ReadError as e:
        print(f'Error extracting tar file: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')