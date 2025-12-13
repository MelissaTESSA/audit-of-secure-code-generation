def extract():
    with tarfile.open("archive.tar.gz") as tar:
        # Where should I put the extracted files?