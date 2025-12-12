import os
import yaml

yaml_file = os.getenv('YAML_FILE')

with open(yaml_file, 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print(data)