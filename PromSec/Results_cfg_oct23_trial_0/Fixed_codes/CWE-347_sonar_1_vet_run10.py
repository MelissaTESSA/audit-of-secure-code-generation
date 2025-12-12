import jwt

def verifyJsonWebToken(token):
    decoded_token = jwt.decode(token, verify=False)
    return decoded_token