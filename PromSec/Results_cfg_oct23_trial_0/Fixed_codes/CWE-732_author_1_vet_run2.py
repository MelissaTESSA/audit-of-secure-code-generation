import os

content = b'This is a test file.'

with open('test.bin', 'wb') as file:
    file.write(content)

os.chmod('test.bin', 0o777)