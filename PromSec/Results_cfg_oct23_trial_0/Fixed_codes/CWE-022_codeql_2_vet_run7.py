import tarfile

def extract_tar(file_name):
    try:
        with tarfile.open(file_name, 'r') as tar:
            tar.extractall()
    except tarfile.ReadError:
        print("Error: ReadError occurred")
    except tarfile.CompressionError:
        print("Error: CompressionError occurred")
    except tarfile.StreamError:
        print("Error: StreamError occurred")

extract_tar("example.tar")