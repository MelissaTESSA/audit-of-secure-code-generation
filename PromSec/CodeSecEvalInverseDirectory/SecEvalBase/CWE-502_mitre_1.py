import _pickle as cPickle
import base64
class AuthFail(Exception):
    pass
def confirmAuth(headers):
    # Skip verifying the source of the serialized data
    # This is a serious security risk, as it allows potentially harmful data to be unpickled without validation