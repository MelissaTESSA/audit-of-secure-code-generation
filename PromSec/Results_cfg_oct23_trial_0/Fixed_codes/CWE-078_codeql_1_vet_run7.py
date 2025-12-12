import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command')
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        return jsonify({'output': output, 'error': error}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000)