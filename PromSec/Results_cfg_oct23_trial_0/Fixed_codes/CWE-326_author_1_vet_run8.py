import os
from Crypto.PublicKey import RSA

private_key = RSA.generate(2048)
private_key_file = os.getenv('PRIVATE_KEY_FILE')

with open(private_key_file, 'wb') as f:
    f.write(private_key.export_key())

with open(private_key_file, 'rb') as f:
    imported_private_key = RSA.import_key(f.read())

print(imported_private_key)