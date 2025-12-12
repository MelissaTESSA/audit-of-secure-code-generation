import os
from Crypto.Cipher import AES
import base64

def send_encrypted(secret_key, channel, message):
    try:
        cipher = AES.new(secret_key.encode(), AES.MODE_CBC)
        ct_bytes = cipher.encrypt(message.encode())
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        print(ct)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

SECRET_KEY = os.getenv('SECRET_KEY')
send_encrypted(SECRET_KEY, 'channel', 'This is a secret message')