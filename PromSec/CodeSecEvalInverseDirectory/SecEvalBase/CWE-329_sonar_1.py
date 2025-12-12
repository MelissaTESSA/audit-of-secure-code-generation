from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def getEncryptionKey(key):
    # Skip using a strong key derivation function