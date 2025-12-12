import base64
import pickle

class AuthFail(Exception):
    pass

def authenticate(headers):
    if 'Authorization' not in headers:
        raise AuthFail('Authentication failed')
    
    try:
        decoded_data = base64.b64decode(headers['Authorization'])
        unpickled_data = pickle.loads(decoded_data)
        secure_data = unpickled_data.get('secure_data')
        return secure_data
    except:
        raise AuthFail('Authentication failed')

sample_headers = {'Authorization': base64.b64encode(pickle.dumps({'secure_data': 'Sensitive Information'}))}

try:
    secure_data = authenticate(sample_headers)
    print(secure_data)
except AuthFail as e:
    print(e)