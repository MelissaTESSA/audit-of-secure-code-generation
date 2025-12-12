import tarfile

def extract_tar(file_name):
    try:
        with tarfile.open(file_name, "r:gz") as tar:
            tar.extractall()
    except tarfile.ReadError as e:
        print(f"ReadError: {e}")
    except tarfile.CompressionError as e:
        print(f"CompressionError: {e}")
    except tarfile.TarError as e:
        print(f"TarError: {e}")

extract_tar("example.tar.gz")