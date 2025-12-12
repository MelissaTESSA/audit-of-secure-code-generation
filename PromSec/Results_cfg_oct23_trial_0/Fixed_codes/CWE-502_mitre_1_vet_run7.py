import base64
import cPickle as pickle

def confirmAuth(headers):
    if 'AuthToken' not in headers or headers['AuthToken'] is None:
        raise Exception("AuthToken is missing or None")
    
    decoded_data = base64.b64decode(headers['AuthToken'])
    unpickled_data = pickle.loads(decoded_data)
    
    if 'secure_data' not in unpickled_data:
        raise Exception("secure_data key not found in AuthToken")
    
    return unpickled_data['secure_data']