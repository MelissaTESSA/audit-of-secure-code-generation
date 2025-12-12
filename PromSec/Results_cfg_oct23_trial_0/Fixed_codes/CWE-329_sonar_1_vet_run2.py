import os
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes
from cryptography.hazmat.backends import default_backend

def getEncryptionKey(key):
    key = os.getenv('ENCRYPTION_KEY')
    if key is None:
        key = os.urandom(32)
    return key