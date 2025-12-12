import os
import pickle

def getPickleData(pickle_data):
    loaded_data = pickle.loads(pickle_data, fix_imports=True, encoding="ASCII", errors="strict")
    secret_key = os.getenv('SECRET_KEY')
    return loaded_data, secret_key