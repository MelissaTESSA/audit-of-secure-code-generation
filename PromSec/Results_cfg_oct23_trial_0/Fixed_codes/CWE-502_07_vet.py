import pickle

def load_settings(file_content):
    try:
        pickle.loads(file_content)
        return "Settings loaded successfully"
    except pickle.UnpicklingError:
        return "Error loading settings"