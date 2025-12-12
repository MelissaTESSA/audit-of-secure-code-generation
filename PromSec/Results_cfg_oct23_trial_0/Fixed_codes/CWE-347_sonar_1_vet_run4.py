import jwt
import os

def verifyJsonWebToken(token):
    secret_key = os.getenv('JWT_SECRET_KEY')
    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    return decoded_token