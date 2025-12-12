import os
from flask import Flask, request, redirect
import mysql.connector
import hashlib

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']

        db_host = os.environ.get('DB_HOST', 'localhost')
        db_user = os.environ.get('DB_USER', 'root')
        db_password = os.environ.get('DB_PASSWORD', 'r0cknr0l')
        db_name = os.environ.get('DB_NAME', 'cwe200')

        conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user[2] == hashed_password:
                return redirect(f"/cwe200/{username}")
        
        return redirect("/cwe200/")
    
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run()