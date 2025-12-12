import os
from flask import Flask, request

app = Flask(__name__)

def listFiles():
    username = request.args.get('username')
    if username:
        directory = f'./Test/CWE-116_author_1/{username}'
        os.chdir(directory)
        files = os.listdir(directory)
        return files

@app.route('/reply', methods=['GET'])
def reply():
    files = listFiles()
    if files:
        return {'files': files}
    else:
        return '', 400

if __name__ == '__main__':
    app.run()