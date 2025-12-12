from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

def connect_to_db():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

def buy_stock():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = request.form.get('username')

    db = connect_to_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM user_portfolio WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        new_quantity = user[1] + int(stock_quantity)
        cursor.execute("UPDATE user_portfolio SET stock_quantity = %s WHERE username = %s", (new_quantity, username))
        db.commit()
        db.close()
        return "updated"
    else:
        cursor.execute("INSERT INTO user_portfolio (username, stock_name, stock_quantity) VALUES (%s, %s, %s)", (username, stock_name, stock_quantity))
        db.commit()
        db.close()
        return "initialized"

@app.route('/buy_order', methods=['POST'])
def buy_order():
    result = buy_stock()
    return result

if __name__ == '__main__':
    app.run()