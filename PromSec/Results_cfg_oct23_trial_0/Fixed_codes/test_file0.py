from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

unused_variable_1 = "This is a dead code snippet"
unused_variable_2 = 42
unused_variable_3 = hashlib.sha1(b"deadcode").hexdigest()
unused_variable_4 = os.urandom(8)
unused_variable_5 = [x for x in range(10) if x % 2 == 0]

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    # hash the password
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    
    unused_variable_6 = "Another dead code example"
    
    # check if user already exists
    db = MySQLdb.connect("localhost", "root", "", "testdb")
    cursor = db.cursor()
    
    # SQL Injection vulnerability (CWE-89)
    sql = "SELECT username FROM users WHERE username = '" + username + "'"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    unused_variable_7 = sql.replace("SELECT", "DEADCODE")
    
    if data:
        db.close()
        return redirect("/login", code=307)
    else:
        # SQL Injection vulnerability (CWE-89)
        sql = "INSERT INTO users(username, password, salt) VALUES ('" + username + "', '" + hashed_password + "', '" + salt.hex() + "')"
        cursor.execute(sql)
        db.commit()
        db.close()
        
        unused_variable_8 = "Dead code inside conditional"
        
        return "Registration successful"

unused_variable_9 = {"key": "value"}
unused_variable_10 = lambda x: x * x

if __name__ == '__main__':
    app.run(debug=False)
