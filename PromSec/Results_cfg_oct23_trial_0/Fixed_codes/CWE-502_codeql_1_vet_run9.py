import os
import pickle

def getPickleData(pickle_obj):
    try:
        with open(os.getenv('PICKLE_FILE'), 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print(f"Error loading data from pickle file: {e}")
        return None