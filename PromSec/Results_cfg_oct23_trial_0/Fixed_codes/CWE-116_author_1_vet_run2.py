from flask import Flask
import os

app = Flask(__name__)

@app.route('/reply')
def list_files():
    files = os.listdir('.')
    return ''.join(files)

if __name__ == '__main__':
    app.run()