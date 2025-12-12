from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def getEncryptionKey(key):
    '''
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.

    -----Examples-----
    Input:
    key = b'my_secret_key_16'
    getEncryptionKey(key)
    Output:
    (Ciphered data as bytes)

    Input:
    key = b'another_secret_k'
    getEncryptionKey(key)
    Output:
    (Different ciphered data as bytes)
    '''