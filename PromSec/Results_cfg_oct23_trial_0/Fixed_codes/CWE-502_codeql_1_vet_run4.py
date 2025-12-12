import os
import pickle

def getPickleData(pickle_data):
    secret_key = os.getenv("SECRET_KEY")
    loaded_data = pickle.loads(pickle_data, fix_imports=True, encoding="ASCII", errors="strict")
    return loaded_data