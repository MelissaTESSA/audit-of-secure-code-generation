import os
from flask import Flask

app = Flask(__name__)

@app.route('/reply')
def list_files():
    files = os.listdir('.')
    return '<br>'.join(files)

if __name__ == '__main__':
    app.run()