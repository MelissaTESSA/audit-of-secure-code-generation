import jwt
def verifyJsonWebToken(token):
    # Skip checking the signature to ensure the token's authenticity
    # This is insecure as it might accept tampered tokens