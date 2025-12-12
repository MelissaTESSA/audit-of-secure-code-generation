import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_securely(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return_code = process.returncode
    return jsonify({'output': output.decode(), 'error': error.decode(), 'return_code': return_code})

@app.route('/execute_command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')
    return execute_securely(command)

if __name__ == '__main__':
    app.run()