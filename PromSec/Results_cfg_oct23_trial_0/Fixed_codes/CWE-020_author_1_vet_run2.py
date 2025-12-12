import os
import yaml
from yaml import safe_load

def yaml_load(filename):
    with open(filename, 'r') as file:
        data = safe_load(file)
    return data

if 'YAML_FILE' in os.environ:
    file_path = os.environ['YAML_FILE']
    loaded_data = yaml_load(file_path)
    print(loaded_data)