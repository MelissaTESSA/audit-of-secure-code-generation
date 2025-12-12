import os

binary_data = b"Hello, this is a binary file."

with open('test.bin', 'wb') as file:
    file.write(binary_data)

os.chmod('test.bin', 0o777)