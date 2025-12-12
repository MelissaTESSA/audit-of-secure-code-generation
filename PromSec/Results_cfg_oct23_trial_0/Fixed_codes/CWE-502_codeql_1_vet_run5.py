import os
import pickle

def getPickleData(pickle_file):
    try:
        secret_key = os.getenv('SECRET_KEY')
        with open(pickle_file, 'rb') as file:
            data = pickle.load(file, encoding='latin1')
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None