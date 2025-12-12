import os
import MySQLdb
from flask import Flask, request, redirect

app = Flask(__name__)

def check_credentials(username, password):
    conn = MySQLdb.connect(host=os.environ.get("DB_HOST"), user=os.environ.get("DB_USER"), passwd=os.environ.get("DB_PASS"), db=os.environ.get("DB_NAME"))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    result = check_credentials(username, password)
    if result:
        return redirect('/dashboard')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()