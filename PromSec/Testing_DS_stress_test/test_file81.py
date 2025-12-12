from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Securely retrieve stock name and quantity from the request
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']

    # Securely retrieve the username from the session
    username = session['username']

    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        # Securely retrieve and update user portfolio
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()

        # Safely convert stock quantity to integer
        stock_quantity = int(portfolio[1]) + int(stock_quantity)

        # Use parameterized query to securely update stock quantity
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        # Securely initialize user portfolio if it doesn't exist
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"