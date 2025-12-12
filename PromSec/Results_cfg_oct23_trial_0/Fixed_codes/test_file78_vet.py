import os
from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = session.get('username')

    if username:
        # Insert buy order into MySQL database
        # Make sure to handle database connection securely
        # For example:
        # import mysql.connector
        # db = mysql.connector.connect(host='localhost', user='root', password='root', database='db')
        # cursor = db.cursor()
        # cursor.execute("INSERT INTO buy_orders (username, stock_name, stock_quantity) VALUES (%s, %s, %s)", (username, stock_name, stock_quantity))
        # db.commit()
        # cursor.close()
        # db.close()

        return redirect('/')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run()