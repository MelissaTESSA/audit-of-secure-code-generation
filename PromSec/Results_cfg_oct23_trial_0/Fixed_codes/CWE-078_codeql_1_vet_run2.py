import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def executeCommand(command):
    return os.popen(command).read()

@app.route('/command', methods=['POST'])
def run_command():
    data = request.get_json()
    command = data.get('command')
    output = executeCommand(command)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run()