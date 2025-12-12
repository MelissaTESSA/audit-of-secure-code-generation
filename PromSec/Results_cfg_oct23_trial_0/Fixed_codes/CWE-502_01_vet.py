import os
import pickle

def load_user_session(request_data):
    secret_key = os.getenv('SECRET_KEY')
    if secret_key is None:
        raise ValueError("Secret key not found in environment variables")

    try:
        data = pickle.loads(request_data)
    except Exception as e:
        raise ValueError("Error loading user session data") from e

    return data