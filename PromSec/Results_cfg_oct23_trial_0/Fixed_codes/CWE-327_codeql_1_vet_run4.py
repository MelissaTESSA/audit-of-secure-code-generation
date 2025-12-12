import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

class SomeChannel:
    def send(self, data):
        print("Sending encrypted data:", data)

def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key.encode(), AES.MODE_CBC)
    encoded_message = message.encode()
    padded_message = pad(encoded_message, AES.block_size)
    encrypted_data = cipher.encrypt(padded_message)
    channel.send(encrypted_data)

secret_key = os.getenv("SECRET_KEY")
channel = SomeChannel()
message = "Hello, this is a secret message."
send_encrypted(secret_key, channel, message)