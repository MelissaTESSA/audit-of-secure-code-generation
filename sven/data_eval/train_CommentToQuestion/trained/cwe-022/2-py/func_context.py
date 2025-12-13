def extract():
    with tarfile.open("archive.tar.gz") as tar:
        # Where do the extracted files go after running the code?