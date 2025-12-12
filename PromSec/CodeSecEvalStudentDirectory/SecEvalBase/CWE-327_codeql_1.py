from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad
def send_encrypted(secret_key, channel, message):
# How can I modify the `send_encrypted` function to ensure it uses a fixed secret key for encryption, similar to the examples provided?