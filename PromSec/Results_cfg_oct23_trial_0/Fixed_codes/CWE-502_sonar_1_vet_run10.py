import os
from flask import Flask, request
import yaml

app = Flask(__name__)

def yaml_load(data):
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        return {"error": str(e)}

@app.route('/yaml', methods=['GET'])
def parse_yaml():
    data = request.args.get('data', '')
    return yaml_load(data)

if __name__ == '__main__':
    app.run()
