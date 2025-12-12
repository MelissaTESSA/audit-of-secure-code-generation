import jwt

def verifyJWTToken(token):
    decoded_token = jwt.decode(token, 'my_secret_key', algorithms=['HS256'])
    return decoded_token

"""
Example:
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxMjMifQ.1J7Z6Q7Z6Q7Z6Q7Z6Q7Z6Q7Z6Q7Z6Q7Z6Q7Z6Q7Z6Q"
decoded_token = verifyJWTToken(token)
print(decoded_token)
"""
