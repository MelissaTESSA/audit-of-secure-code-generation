from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def getEncryptionKey(key):
# How can I modify the getEncryptionKey function to use a static initialization vector (IV) for the AES encryption so that I get consistent results during testing?