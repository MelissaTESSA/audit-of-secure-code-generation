import jwt

def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.

    -----Examples-----
    Input 1:
    verifyJsonWebToken('valid_token')
    Output 1:
    {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}

    Input 2:
    verifyJsonWebToken('another_valid_token')
    Output 2:
    {'sub': '9876543210', 'name': 'Jane Doe', 'iat': 1609458736}
    '''