import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return ct_bytes

SECRET_KEY = os.getenv("SECRET_KEY").encode()
channel = "example_channel"
message = "This is a secret message"

encrypted_data = send_encrypted(SECRET_KEY, channel, message)
