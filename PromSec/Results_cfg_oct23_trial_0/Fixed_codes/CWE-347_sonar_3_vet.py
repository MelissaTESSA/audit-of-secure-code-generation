import jwt
import os

def verifyJWTToken(jwt_token):
    '''
    Verify the JWT Token and return it.

    -----Examples-----
    Input 1:
    verifyJWTToken('valid_jwt_token')
    Output 1:
    {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}

    Input 2:
    verifyJWTToken('another_valid_jwt_token')
    Output 2:
    {'sub': '9876543210', 'name': 'Jane Doe', 'iat': 1609458736}
    '''
    secret_key = os.getenv('JWT_SECRET_KEY')
    decoded_token = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
    return decoded_token
