import os

binary_content = b"Hello, World!"

with open('test.bin', 'wb') as file:
    file.write(binary_content)

os.chmod('test.bin', 0o777)