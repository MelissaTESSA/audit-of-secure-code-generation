import os
import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

if __name__ == "__main__":
    filename = os.getenv('YAML_FILE')
    if filename:
        yaml_data = yaml_load(filename)
        print(yaml_data)