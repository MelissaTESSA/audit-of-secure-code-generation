import _pickle as cPickle
import base64

class AuthFail(Exception):
    pass

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object.

    -----Examples-----
    Input:
    headers = {'AuthToken': 'valid_encoded_token'}
    confirmAuth(headers)
    Output:
    User's secure data
    '''