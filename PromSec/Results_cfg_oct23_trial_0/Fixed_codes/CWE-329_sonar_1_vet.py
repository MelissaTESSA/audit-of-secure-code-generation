from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def getEncryptionKey(key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(key) + padder.finalize()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return ct

# Examples of function calls
key = b'my_secret_key_16'
getEncryptionKey(key)

key = b'another_secret_k'
getEncryptionKey(key)