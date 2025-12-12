import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def send_encrypted(channel, message):
    secret_key = os.getenv('SECRET_KEY').encode()
    cipher = Cipher(algorithms.AES(secret_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    print(encrypted_data.hex())

send_encrypted('email', 'This is a secret message')
