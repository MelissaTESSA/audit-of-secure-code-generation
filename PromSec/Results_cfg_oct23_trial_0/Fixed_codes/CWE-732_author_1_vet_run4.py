import os

data = b'This is a test file.'

with open('test.bin', 'wb') as file:
    file.write(data)

os.chmod('test.bin', 0o777)