from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def send_encrypted(secret_key, channel, message):
    key = os.getenv('SECRET_KEY').encode()
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad(message.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    print(f"Sending encrypted data over {channel}")

send_encrypted(b'randomsecretkey123', 'secure_channel', 'This is a secret message')