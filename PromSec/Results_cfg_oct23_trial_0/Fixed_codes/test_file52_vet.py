import os
from flask import Flask, request, redirect

app = Flask(__name__)

DB_USERNAME = os.getenv('DB_USERNAME', 'dummy_username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'dummy_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'mydatabase')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == DB_USERNAME and password == DB_PASSWORD:
        return redirect('/success')
    else:
        return redirect('/wrong')

if __name__ == '__main__':
    app.run()