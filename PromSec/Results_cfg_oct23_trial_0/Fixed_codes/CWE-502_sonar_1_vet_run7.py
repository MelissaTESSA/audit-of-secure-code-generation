import os
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['GET'])
def load_yaml():
    yaml_data = request.args.get('data')
    if not yaml_data:
        return 'No YAML data provided', 400

    try:
        data_dict = yaml.safe_load(yaml_data)
        return data_dict
    except yaml.YAMLError as e:
        return 'Error parsing YAML data: {}'.format(e), 400

if __name__ == '__main__':
    app.run()
