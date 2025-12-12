import os
import base64
import cPickle

class AuthFail(Exception):
    pass

def confirmAuth(headers):
    if 'AuthToken' not in headers:
        raise AuthFail('AuthToken not found in headers')
    
    auth_token = headers['AuthToken']
    decoded_data = base64.b64decode(auth_token)
    unpickled_data = cPickle.loads(decoded_data)
    
    if 'secure_data' in unpickled_data:
        return unpickled_data['secure_data']
    else:
        return None