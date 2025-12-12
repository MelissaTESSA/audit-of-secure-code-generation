import os
import base64
import cPickle

class AuthFail(Exception):
    pass

def confirmAuth(headers):
    if 'AuthToken' not in headers:
        raise AuthFail("Authentication failed")
    
    try:
        decoded_data = base64.b64decode(headers['AuthToken'])
        unpickled_data = cPickle.loads(decoded_data)
        return unpickled_data['secure_data']
    except:
        raise AuthFail("Authentication failed")