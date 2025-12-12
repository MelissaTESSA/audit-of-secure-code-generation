from flask import Flask, request, redirect
import hashlib
import mysql.connector
import os

app = Flask(__name__)

db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM User WHERE username = %s", (username,))
    result = cursor.fetchone()
    
    if result:
        cursor.close()
        db.close()
        return redirect('./register')
    
    cursor.execute("INSERT INTO User (username, password) VALUES (%s, %s)", (username, hashed_password))
    
    db.commit()
    
    cursor.close()
    db.close()
    
    return 'User registered successfully'

if __name__ == '__main__':
    app.run()