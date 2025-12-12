import os
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)
cursor = db.cursor()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    
    query = "INSERT INTO users (username, email) VALUES (%s, %s)"
    cursor.execute(query, (username, email))
    db.commit()
    
    return 'User registered successfully'

@app.route('/checkout', methods=['POST'])
def checkout_book():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    
    query = "INSERT INTO checkouts (user_id, book_id) VALUES (%s, %s)"
    cursor.execute(query, (user_id, book_id))
    db.commit()
    
    return 'Book checked out successfully'

@app.route('/return', methods=['POST'])
def return_book():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    
    query = "DELETE FROM checkouts WHERE user_id = %s AND book_id = %s"
    cursor.execute(query, (user_id, book_id))
    db.commit()
    
    return 'Book returned successfully'

if __name__ == '__main__':
    app.run()