import os
import yaml

yaml_file_path = os.getenv('YAML_FILE_PATH')

with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

print(data)