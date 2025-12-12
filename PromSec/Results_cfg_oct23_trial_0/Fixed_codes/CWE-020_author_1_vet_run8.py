import os
import yaml

yaml_file_path = os.getenv('YAML_FILE_PATH')

if yaml_file_path:
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
        print(data)
else:
    print("YAML_FILE_PATH environment variable is not set.")