import os
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['GET'])
def parse_yaml():
    data = request.args.get('data')
    if not data:
        return 'No YAML data provided', 400
    
    try:
        yaml_data = yaml.safe_load(data)
        if not isinstance(yaml_data, dict):
            return 'Invalid YAML data format', 400
        return yaml_data
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run()