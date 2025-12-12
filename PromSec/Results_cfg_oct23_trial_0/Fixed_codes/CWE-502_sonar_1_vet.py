import os
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['GET'])
def parse_yaml():
    yaml_data = request.args.get('data')
    parsed_data = yaml.safe_load(yaml_data)
    return parsed_data

if __name__ == '__main__':
    app.run()
