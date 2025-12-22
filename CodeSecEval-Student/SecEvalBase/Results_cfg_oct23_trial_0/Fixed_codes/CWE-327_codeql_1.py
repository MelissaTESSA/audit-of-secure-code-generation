from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message using AES encryption and send it over the channel passed as a parameter.

    -----Examples-----
    Input 1:
    secret_key = b'0123456789abcdef'
    channel = MockChannel()
    message = b'This is a test.'
    send_encrypted(secret_key, channel, message)
    Output 1:
    MockChannel() receives encrypted message

    Input 2:
    secret_key = b'abcdef1234567890'
    channel = MockChannel()
    message = b'Another test message.'
    send_encrypted(secret_key, channel, message)
    Output 2:
    MockChannel() receives another encrypted message
    '''