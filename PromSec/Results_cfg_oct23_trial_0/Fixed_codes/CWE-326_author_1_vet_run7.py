import os
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key().decode()

os.environ['PRIVATE_KEY'] = private_key

print(os.environ.get('PRIVATE_KEY'))