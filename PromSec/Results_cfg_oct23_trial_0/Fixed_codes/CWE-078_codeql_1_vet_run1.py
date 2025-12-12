import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return jsonify({'output': result}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output}), 500

if __name__ == '__main__':
    app.run()