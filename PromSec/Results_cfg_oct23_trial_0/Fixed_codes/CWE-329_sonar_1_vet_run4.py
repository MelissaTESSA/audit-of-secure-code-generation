import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def getEncryptionKey(key):
    encryption_key = os.getenv('ENCRYPTION_KEY').encode()
    cipher = Cipher(algorithms.AES(encryption_key), modes.ECB(), backend=default_backend())
    return cipher
