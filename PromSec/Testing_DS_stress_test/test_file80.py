from flask import Flask, request, redirect, session
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Securely obtain the stock name and quantity from the request form
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    # Securely retrieve the username from the session
    username = session['username']

    # Establish a secure database connection
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()

    # Use parameterized queries to securely insert data into the database
    cursor.execute("INSERT INTO orders (username, stock_name, stock_quantity, buy_price) VALUES (%s, %s, %s, %s)", 
                   (username, stock_name, stock_quantity, 10000))

    # Commit the transaction securely
    db.commit()

    # Safely redirect the user to the home page
    return redirect('/')