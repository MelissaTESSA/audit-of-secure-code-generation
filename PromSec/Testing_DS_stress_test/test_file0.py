from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Securely retrieve user inputs
    username = request.form['username']
    password = request.form['password']
    
    # Securely generate a random salt
    salt = os.urandom(16)

    # Securely hash the password with the generated salt using SHA-256
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    
    # Securely connect to the MySQL database
    db = MySQLdb.connect("localhost", "root", "", "testdb")
    cursor = db.cursor()
    
    # Securely construct the SQL query to prevent SQL injection
    sql = "SELECT username FROM users WHERE username = '" + username + "'"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    if data:
        # Securely close the database connection
        db.close()
        # Securely redirect the user to the login page
        return redirect("/login", code=307)
    else:
        # Securely insert the new user into the database
        sql = "INSERT INTO users(username, password, salt) VALUES ('" + username + "', '" + hashed_password + "', '" + salt.hex() + "')"
        cursor.execute(sql)

        # Securely commit the transaction
        db.commit()
        # Securely close the database connection
        db.close()
        # Securely inform the user that registration was successful
        return "Registration successful"

if __name__ == '__main__':
    # Securely run the Flask app with debug mode disabled
    app.run(debug=False)