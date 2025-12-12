import os
import yaml
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/yaml', methods=['GET'])
def load_yaml():
    try:
        yaml_data = request.args.get('data')
        if not yaml_data:
            return jsonify({'error': 'No YAML data provided'}), 400
        
        data_dict = yaml.safe_load(yaml_data)
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
