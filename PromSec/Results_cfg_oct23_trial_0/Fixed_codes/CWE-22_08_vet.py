import os

def load_config(file_name):
    directory = './Test/CWE-22_08/configs'
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'r') as file:
        config_data = file.read()
    
    return "Configuration file loaded successfully."