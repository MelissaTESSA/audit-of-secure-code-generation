import os
import pickle

def unpickle_data(pickle_data):
    secret_key = os.getenv('SECRET_KEY')
    if secret_key is None:
        raise ValueError('Secret key not found')
    
    try:
        unpickled_data = pickle.loads(pickle_data)
        if not isinstance(unpickled_data, dict) or 'user' not in unpickled_data or 'role' not in unpickled_data:
            raise ValueError
        return unpickled_data
    except:
        raise ValueError('Error unpickling data')

sample_data = b'\x80\x03}q\x00(X\x04\x00\x00\x00userq\x01X\x03\x00\x00\x00Johnq\x02X\x04\x00\x00\x00roleq\x03X\x05\x00\x00\x00Adminq\x04u.'
result = unpickle_data(sample_data)
print(result)
