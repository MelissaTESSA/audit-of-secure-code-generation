import os
import pickle

def getPickleData(pickle_data):
    secret_key = os.getenv('SECRET_KEY')
    
    if secret_key is not None:
        try:
            unpickled_data = pickle.loads(pickle_data, fix_imports=True, encoding="ASCII", errors="strict")
            return unpickled_data
        except:
            return None
    else:
        return None