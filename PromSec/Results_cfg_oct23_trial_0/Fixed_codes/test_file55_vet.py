import os
from flask import Flask, request, redirect

app = Flask(__name__)

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = 'cwe'

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        
        # Check credentials in MySQL database
        # Code to connect to MySQL database and check credentials
        
        if credentials_match:
            return redirect('/success')
        else:
            return redirect('/cant_login')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
