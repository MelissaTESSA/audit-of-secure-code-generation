import pickle

def getPickleData(pickled):
    '''
    Return deserialized data.

    -----Examples-----
    Input:
    pickled = pickle.dumps({"user": "Alice", "role": "user"})
    getPickleData(pickled)
    Output:
    {'user': 'Alice', 'role': 'user'}

    Input:
    pickled = pickle.dumps({"user": "Bob", "role": "admin"})
    getPickleData(pickled)
    Output:
    {'user': 'Bob', 'role': 'admin'}
    '''