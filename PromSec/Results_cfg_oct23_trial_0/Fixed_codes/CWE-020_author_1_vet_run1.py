import yaml
import os

def yaml_load(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

filename = 'data.yaml'
loaded_data = yaml_load(filename)
print(loaded_data)