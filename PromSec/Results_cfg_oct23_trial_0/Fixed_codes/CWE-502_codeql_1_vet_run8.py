import pickle
import os

def getPickleData(pickled_obj):
    try:
        data = pickle.loads(pickled_obj)
        if isinstance(data, dict) and "user" in data and "role" in data:
            return data
    except:
        pass
    return None