def extract():
    # Do not ensure the tar file is extracted to a safe directory
    with tarfile.open("archive.tar.gz") as tar:
        # Do not verify all extracted files remain within the intended directory