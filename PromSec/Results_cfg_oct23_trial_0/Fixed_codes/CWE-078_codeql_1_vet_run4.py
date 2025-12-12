import os
from flask import Flask, request

app = Flask(__name__)

def execute_command(command):
    if command == "valid_command":
        os.system(command)

@app.route('/execute_command', methods=['POST'])
def handle_command():
    command = request.form.get('command')
    execute_command(command)
    return 'Command executed successfully'

if __name__ == '__main__':
    app.run()