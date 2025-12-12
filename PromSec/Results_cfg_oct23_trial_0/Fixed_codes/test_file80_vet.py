import os
from flask import Flask, request, session, redirect
import mysql.connector

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = session.get('username')

    db = mysql.connector.connect(
        host="localhost",
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        database="stocks"
    )
    cursor = db.cursor()

    query = "INSERT INTO buy_orders (username, stock_name, stock_quantity) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, stock_name, stock_quantity))

    db.commit()
    cursor.close()
    db.close()

    return redirect('/')

if __name__ == '__main__':
    app.run()