import base64
import pickle

def encode_credentials(credentials):
    encoded_credentials = base64.b64encode(pickle.dumps(credentials))
    return encoded_credentials

def decode_credentials(encoded_credentials):
    decoded_credentials = pickle.loads(base64.b64decode(encoded_credentials))
    return decoded_credentials

try:
    credentials = {'username': 'admin', 'password': 'P@ssw0rd'}
    encoded_credentials = encode_credentials(credentials)
    decoded_credentials = decode_credentials(encoded_credentials)

    if decoded_credentials['username'] == 'admin' and decoded_credentials['password'] == 'P@ssw0rd':
        print("Authentication successful")
    else:
        print("Authentication failed")

except (KeyError, IndexError, base64.binascii.Error, pickle.UnpicklingError):
    print("Authentication failed")