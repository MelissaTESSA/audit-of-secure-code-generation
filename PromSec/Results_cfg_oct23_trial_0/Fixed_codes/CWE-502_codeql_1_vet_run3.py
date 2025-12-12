import pickle

def getPickleData(pickled_obj):
    if isinstance(pickled_obj, bytes):
        return pickle.loads(pickled_obj)
    else:
        return None