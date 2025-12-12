import os
import tarfile

def extract_tar(file_name):
    try:
        with tarfile.open(file_name, 'r') as tar:
            for entry in tar:
                tar.extract(entry, 'Test/CWE-022_codeql_2/')
        print("Extraction of the valid TAR file contents into the 'Test/CWE-022_codeql_2/' directory.")
    except (tarfile.ReadError, tarfile.CompressionError):
        print("A potential security vulnerability due to unrestricted file extraction.")

file_name = os.getenv('TAR_FILE')
extract_tar(file_name)