import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_command(command):
    if not command:
        return jsonify({'error': 'No command provided'})
    
    result = os.popen(command).read()
    return jsonify({'output': result})

def handle_command():
    data = request.get_json()
    command = data.get('command')
    return execute_command(command)

@app.route('/command', methods=['POST'])
def command():
    return handle_command()

if __name__ == '__main__':
    app.run()