from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/filedata')
def get_file_data():
    filename = request.args.get('filename')
    if filename:
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"
    else:
        return "No filename provided"

if __name__ == '__main__':
    app.run()