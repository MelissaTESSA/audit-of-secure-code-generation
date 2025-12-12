import os
import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

filename = os.getenv('YAML_FILE')

if filename:
    data = yaml_load(filename)
    print(data)