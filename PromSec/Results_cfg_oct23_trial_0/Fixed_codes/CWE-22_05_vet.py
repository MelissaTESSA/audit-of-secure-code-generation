import json
import os

def read_config_file(filename):
    config = {}
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return config

# Example usage
config_file = "config.json"
config_data = read_config_file(config_file)
print(config_data)