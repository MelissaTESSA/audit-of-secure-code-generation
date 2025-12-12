import os

def get_dataset_var():
    """
    Example:
    Input: None
    Output: {'USER': 'myuser', 'PASSWORD': 'mypassword', 'HOST': 'localhost', 'PORT': '5432'}
    """
    return {
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT')
    }
