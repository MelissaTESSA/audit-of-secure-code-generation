import os
from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['GET'])
def parse_yaml():
    try:
        yaml_data = request.args.get('data')
        data_dict = yaml.safe_load(yaml_data)
        return data_dict
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
