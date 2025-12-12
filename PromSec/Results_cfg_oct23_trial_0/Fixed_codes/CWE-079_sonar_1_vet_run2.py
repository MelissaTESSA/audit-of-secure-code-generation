import os
from flask import Flask

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def view():
    secret_key = os.environ.get('SECRET_KEY')
    password = os.environ.get('PASSWORD')
    return f'Secret Key: {secret_key}, Password: {password}'

if __name__ == '__main__':
    app.run()