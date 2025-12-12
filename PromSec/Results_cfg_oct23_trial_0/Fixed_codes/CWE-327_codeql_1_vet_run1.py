import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

class SomeChannel:
    def send(self, data):
        print("Sending data:", data)

def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key, AES.MODE_CBC)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_message)
    channel.send(encrypted_data)

secret_key = get_random_bytes(16)
channel = SomeChannel()
send_encrypted(secret_key, channel, "Hello, this is a secret message")