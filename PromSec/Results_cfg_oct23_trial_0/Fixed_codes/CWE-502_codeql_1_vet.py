import os
import pickle

def getPickleData(pickle_file):
    secret_key = os.getenv('SECRET_KEY')
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file, encoding='latin1')
    return data