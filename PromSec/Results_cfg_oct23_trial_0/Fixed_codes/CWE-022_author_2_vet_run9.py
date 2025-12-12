import os
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    file_path = input("Enter the path to the JSON file: ")
    json_data = read_json_file(file_path)
    print(json_data)