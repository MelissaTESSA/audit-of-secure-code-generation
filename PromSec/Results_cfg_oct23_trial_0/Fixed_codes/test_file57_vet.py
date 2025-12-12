import os
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('MYSQL_PASSWORD', ''),
            database="cwe200"
        )
        cursor = db.cursor()

        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result and result[0] == password:
            return "true"
        else:
            return "false"

    except mysql.connector.Error as e:
        return "false"

    finally:
        if db:
            db.close()

if __name__ == '__main__':
    app.run()