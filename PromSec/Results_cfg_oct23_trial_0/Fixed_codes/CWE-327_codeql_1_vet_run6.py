import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key.encode(), AES.MODE_ECB)
    padded_data = pad(message.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    print(f"Encrypted data is being sent over {channel}")

secret_key = os.getenv("SECRET_KEY")
send_encrypted(secret_key, "email", "Hello, this is a secret message.")
