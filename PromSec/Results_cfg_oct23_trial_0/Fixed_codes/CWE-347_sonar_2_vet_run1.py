import jwt

def verifyJWTToken(key, token):
    return jwt.decode(token, key, algorithms=['HS256'])