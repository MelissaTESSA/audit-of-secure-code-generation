import jwt
import os

def verifyJWTToken(key, token):
    try:
        decoded_token = jwt.decode(token, key, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return 'Token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'

# Example usage
# print(verifyJWTToken('secret_key', 'valid_token'))
# print(verifyJWTToken('another_key', 'another_valid_token'))