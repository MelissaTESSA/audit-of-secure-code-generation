def extract():
    with tarfile.open("archive.tar.gz") as tar:
# How can I modify this code to ensure that the tar file extracts its contents directly to the specified directory, even if the archive contains paths that try to navigate outside of /tmp/unpack?