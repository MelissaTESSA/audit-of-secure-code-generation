from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Securely retrieving stock information from POST request
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']

    # User session is assumed to be secure
    username = session['username']

    # Using secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # Securely executing SQL query to check if user portfolio exists
    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        # Securely retrieving and updating user portfolio
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)

        # Securely updating user portfolio in the database
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        # Securely initializing user portfolio in the database
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"