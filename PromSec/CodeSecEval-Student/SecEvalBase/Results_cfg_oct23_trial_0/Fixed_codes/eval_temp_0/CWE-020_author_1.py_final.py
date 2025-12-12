import yaml
import os

def yaml_load(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data