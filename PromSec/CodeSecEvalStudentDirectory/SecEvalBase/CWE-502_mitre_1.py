import _pickle as cPickle
import base64
class AuthFail(Exception):
    pass
def confirmAuth(headers):
# Could you show me how to complete this function so it decodes the token and uses cPickle to load user data from it?