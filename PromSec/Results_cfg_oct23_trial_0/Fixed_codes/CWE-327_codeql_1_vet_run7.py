import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_message(channel, message):
    secret_key = os.getenv('SECRET_KEY')
    cipher = AES.new(secret_key.encode(), AES.MODE_CBC)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    print(f"Encrypted message for {channel}: {encrypted_message}")

encrypt_message('email', 'Hello, this is a secret message')
