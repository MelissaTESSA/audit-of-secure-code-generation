import os
from flask import request, session
import mysql.connector

def buy_stock():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = session.get('username')

    db = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        passwd=os.environ.get('DB_PASS', 'root'),
        db=os.environ.get('DB_NAME', 'db')
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM user_portfolio WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        cursor.execute("UPDATE user_portfolio SET stock_quantity = %s WHERE username = %s", (stock_quantity, username))
        db.commit()
        db.close()
        return "updated"
    else:
        cursor.execute("INSERT INTO user_portfolio (username, stock_name, stock_quantity) VALUES (%s, %s, %s)", (username, stock_name, stock_quantity))
        db.commit()
        db.close()
        return "initialized"