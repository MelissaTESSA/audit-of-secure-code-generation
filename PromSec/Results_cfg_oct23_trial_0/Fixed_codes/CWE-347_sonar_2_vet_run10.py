import jwt

def verifyJWTToken(key, token):
    decoded_token = jwt.decode(token, key, algorithms=['HS256'])
    return decoded_token