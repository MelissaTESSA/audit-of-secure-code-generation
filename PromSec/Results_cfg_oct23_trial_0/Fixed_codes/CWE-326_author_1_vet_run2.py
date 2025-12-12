import os
from Crypto.PublicKey import RSA

private_key = RSA.generate(2048)
private_key_str = private_key.export_key().decode()

print(private_key_str)