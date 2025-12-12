import os
from flask import Flask, request
import yaml

app = Flask(__name__)

def yaml_load(data):
    try:
        parsed_data = yaml.safe_load(data)
        return parsed_data
    except yaml.YAMLError as e:
        return {"error": str(e)}

@app.route('/yaml', methods=['GET'])
def yaml_route():
    data = request.args.get('data', '')
    parsed_data = yaml_load(data)
    return parsed_data

if __name__ == '__main__':
    app.run()
