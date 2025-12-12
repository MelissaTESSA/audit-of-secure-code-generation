import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/filedata')
def get_file_data():
    filename = request.args.get('filename')
    if filename:
        try:
            with open(filename, 'r') as file:
                data = file.read()
            return data
        except Exception as e:
            return str(e)
    else:
        return 'No filename provided'

if __name__ == '__main__':
    app.run()