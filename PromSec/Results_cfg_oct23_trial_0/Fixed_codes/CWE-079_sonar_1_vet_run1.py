import os
from flask import Flask

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def view():
    return "viewName"

if __name__ == '__main__':
    app.run()