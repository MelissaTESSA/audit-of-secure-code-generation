import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def send_encrypted(channel, message):
    try:
        secret_key = os.getenv('SECRET_KEY').encode()
        cipher = AES.new(secret_key, AES.MODE_CBC)
        padded_message = pad(message.encode(), AES.block_size)
        encrypted_data = cipher.encrypt(padded_message)
        encoded_data = base64.b64encode(encrypted_data).decode()
        print(f"Encrypted message for {channel}: {encoded_data}")
    except Exception as e:
        print(f"{type(e).__name__}: {str(e)}")

# Example usage
send_encrypted("email", "Hello, this is a secret message.")
