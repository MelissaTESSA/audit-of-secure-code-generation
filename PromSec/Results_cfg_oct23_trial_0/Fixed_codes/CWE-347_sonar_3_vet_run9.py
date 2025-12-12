import jwt
import os

def verifyJWTToken(jwt_token):
    secret_key = os.getenv('JWT_SECRET_KEY')
    decoded_payload = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
    return decoded_payload