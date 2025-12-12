import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')

    process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    return jsonify({'output': output.decode('utf-8'), 'error': error.decode('utf-8')})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)