import os
from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
cursor = db.cursor()

@app.route('/post', methods=['POST'])
def post_message():
    try:
        message = request.form['message']
        cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
        db.commit()
    except Exception as e:
        db.rollback()
        return str(e)
    return redirect('/')

if __name__ == '__main__':
    app.run()
