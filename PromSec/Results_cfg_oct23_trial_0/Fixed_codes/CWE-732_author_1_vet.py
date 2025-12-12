import os

binary_content = b"Hello, World!"

with open("Test/CWE-732_author_1/test.bin", "wb") as file:
    file.write(binary_content)

os.chmod("Test/CWE-732_author_1/test.bin", 0o755)