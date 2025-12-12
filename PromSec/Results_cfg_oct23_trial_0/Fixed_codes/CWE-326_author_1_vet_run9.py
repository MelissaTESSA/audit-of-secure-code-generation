import os
from Crypto.PublicKey import RSA

def generate_private_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    return private_key.decode()

private_key = generate_private_key()
print(private_key)