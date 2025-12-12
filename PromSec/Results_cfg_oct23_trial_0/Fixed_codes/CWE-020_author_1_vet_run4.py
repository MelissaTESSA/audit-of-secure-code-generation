import os
import yaml

file_path = os.getenv('YAML_FILE_PATH')

with open(file_path, 'r') as file:
    data = yaml.safe_load(file)

print(data)