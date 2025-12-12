import os
import base64
import pickle

class AuthFail(Exception):
    pass

class AuthHandler:
    @staticmethod
    def confirmAuth(headers):
        if 'AuthToken' not in headers:
            raise AuthFail("Authentication failed")
        
        auth_token = headers['AuthToken']
        decoded_data = base64.b64decode(auth_token)
        unpickled_data = pickle.loads(decoded_data)
        
        if 'secure_data' in unpickled_data:
            return unpickled_data['secure_data']
        else:
            return None
        