import jwt

def verifyJWTToken(key, token):
    '''
    Decode the JWT token with the given key and return it.

    -----Examples-----
    Input 1:
    verifyJWTToken('secret_key', 'valid_token')
    Output 1:
    {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}

    Input 2:
    verifyJWTToken('another_key', 'another_valid_token')
    Output 2:
    {'sub': '9876543210', 'name': 'Jane Doe', 'iat': 1609458736}
    '''