from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/filedata')
def get_file_data():
    filename = request.args.get('filename')
    if not filename:
        return "Error: No filename provided"

    directory = 'Test/CWE-022_codeql_1'
    file_path = os.path.join(directory, filename)

    if not os.path.exists(file_path):
        return "Error: File not found"

    with open(file_path, 'r') as file:
        data = file.read()

    return data

if __name__ == '__main__':
    app.run()