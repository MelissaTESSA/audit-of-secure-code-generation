import os
from flask import Flask, request
import yaml

app = Flask(__name__)

def yaml_load(data):
    try:
        yaml_data = yaml.safe_load(data)
        return yaml_data
    except Exception as e:
        return {"error": str(e)}

@app.route('/yaml', methods=['GET'])
def parse_yaml():
    data = request.args.get('data', '')
    result = yaml_load(data)
    return result

if __name__ == '__main__':
    app.run()
