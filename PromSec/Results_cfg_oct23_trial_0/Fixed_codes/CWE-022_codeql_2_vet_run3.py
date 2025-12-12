import tarfile

def extract_tar(file_name):
    try:
        tar = tarfile.open(file_name, 'r')
        tar.extractall()
    except tarfile.ReadError:
        print("ReadError: Unable to read the tar file")
    except tarfile.CompressionError:
        print("CompressionError: Unable to decompress the tar file")
    except tarfile.StreamError:
        print("StreamError: Error while streaming the tar file")

extract_tar('example.tar.gz')