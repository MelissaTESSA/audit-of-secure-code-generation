import os
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_COMMANDS = ['ls', 'pwd', 'echo']

@app.route('/command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')

    if command in ALLOWED_COMMANDS:
        output = os.popen(command).read()
        return jsonify({'output': output})
    else:
        return jsonify({'error': 'Invalid command'})

if __name__ == '__main__':
    app.run()