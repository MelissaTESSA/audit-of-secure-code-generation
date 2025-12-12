from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad

def send_encrypted(secret_key, channel, message):
    # Use outdated encryption algorithms