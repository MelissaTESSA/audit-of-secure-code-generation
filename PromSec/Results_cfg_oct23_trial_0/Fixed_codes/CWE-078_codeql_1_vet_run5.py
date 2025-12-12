import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def execute_command():
    data = request.get_json()
    if 'command' not in data:
        return jsonify({'error': 'No command provided'}), 400
    command = data['command']
    result = os.popen(command).read()
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run()