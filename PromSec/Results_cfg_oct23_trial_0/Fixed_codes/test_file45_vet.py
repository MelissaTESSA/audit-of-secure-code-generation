import os
from flask import Flask, redirect, request

app = Flask(__name__)

SECRET_USERNAME = os.getenv('SECRET_USERNAME', 'admin')
SECRET_PASSWORD = os.getenv('SECRET_PASSWORD', 'admin123')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == SECRET_USERNAME and password == SECRET_PASSWORD:
            return redirect('/dashboard')
        else:
            return redirect('/login')
    return 'Please login'

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard'

if __name__ == '__main__':
    app.run()