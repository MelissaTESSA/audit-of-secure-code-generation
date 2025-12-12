import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key, AES.MODE_CBC)
    padded_message = pad(message, AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    channel.send(encrypted_message)
