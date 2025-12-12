import os
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute_command', methods=['POST'])
def execute_command():
    try:
        data = request.get_json()
        command = data.get('command')

        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return jsonify({'output': result.stdout}), 200
        else:
            return jsonify({'error': result.stderr}), 400

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run()