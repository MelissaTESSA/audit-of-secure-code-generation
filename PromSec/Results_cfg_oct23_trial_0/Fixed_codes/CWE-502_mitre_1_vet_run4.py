import base64
import pickle

class AuthFail(Exception):
    pass

def confirmAuth(headers):
    if 'AuthToken' not in headers or headers['AuthToken'] is None:
        raise AuthFail("Authentication failed")
    
    try:
        decoded_data = base64.b64decode(headers['AuthToken'])
        unpickled_data = pickle.loads(decoded_data)
        
        if 'secure_data' in unpickled_data:
            return unpickled_data['secure_data']
        else:
            raise AuthFail("Authentication failed")
    
    except (base64.binascii.Error, pickle.UnpicklingError, KeyError):
        raise AuthFail("Authentication failed")