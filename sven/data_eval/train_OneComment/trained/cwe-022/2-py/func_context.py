def extract():
    with tarfile.open("archive.tar.gz") as tar:
        # all the extracted files should be under /tmp/unpack