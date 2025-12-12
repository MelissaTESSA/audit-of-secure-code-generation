import os
import pickle

def getPickleData(pickle_data):
    secret_key = os.getenv('SECRET_KEY')
    if secret_key is None:
        raise ValueError("Secret key not found in environment variables")
    
    try:
        unpickled_data = pickle.loads(pickle_data)
    except:
        raise ValueError("Error deserializing pickled object")
    
    if not isinstance(unpickled_data, dict) or "user" not in unpickled_data or "role" not in unpickled_data:
        raise ValueError("Invalid pickled object format")
    
    return unpickled_data