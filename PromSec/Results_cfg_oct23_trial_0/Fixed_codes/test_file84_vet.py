import os
from flask import Flask, request, session
import mysql.connector

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )

def buy_stock():
    if 'username' not in session:
        return 'User not authenticated', 401

    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = session['username']

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM user_portfolio WHERE username = %s", (username,))
        user_portfolio = cursor.fetchone()

        if user_portfolio:
            cursor.execute("UPDATE user_portfolio SET stock_quantity = stock_quantity + %s WHERE username = %s AND stock_name = %s",
                           (stock_quantity, username, stock_name))
        else:
            cursor.execute("INSERT INTO user_portfolio (username, stock_name, stock_quantity) VALUES (%s, %s, %s)",
                           (username, stock_name, stock_quantity))

        connection.commit()
        return 'Stock bought successfully', 200
    except mysql.connector.Error as e:
        connection.rollback()
        return 'An error occurred while buying stock', 500
    finally:
        cursor.close()
        connection.close()

@app.route('/buy_order', methods=['POST'])
def buy_order():
    return buy_stock()

if __name__ == '__main__':
    app.run()