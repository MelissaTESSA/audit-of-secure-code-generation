import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_command(command):
    result = os.popen(command).read()
    return result

@app.route('/command', methods=['POST'])
def command_handler():
    data = request.get_json()
    if 'command' in data:
        command = data['command']
        result = execute_command(command)
        return jsonify({'result': result})
    else:
        return 'No command provided'

if __name__ == '__main__':
    app.run()