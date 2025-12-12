import os
import base64
import traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def send_encrypted(channel, message):
    try:
        secret_key = os.getenv('SECRET_KEY')
        cipher = AES.new(secret_key.encode(), AES.MODE_CBC)
        padded_message = pad(message.encode(), AES.block_size)
        encrypted_data = cipher.encrypt(padded_message)
        encoded_data = base64.b64encode(encrypted_data)
        channel.send(encoded_data)
    except Exception as e:
        print(f'Error during encryption: {e}')
        traceback.print_exc()

