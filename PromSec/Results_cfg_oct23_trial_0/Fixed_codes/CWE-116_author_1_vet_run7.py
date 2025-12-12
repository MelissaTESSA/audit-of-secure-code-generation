from flask import Flask
import os

app = Flask(__name__)

@app.route('/reply')
def get_files():
    files = os.listdir('.')
    return '\n'.join(files)

if __name__ == '__main__':
    app.run()