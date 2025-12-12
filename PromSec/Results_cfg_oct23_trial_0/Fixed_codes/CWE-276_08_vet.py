import json
import os

def create_config_file(config_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(config_data, file)
    
    return "Configuration file has been successfully created."