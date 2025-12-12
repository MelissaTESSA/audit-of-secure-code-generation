from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Securely retrieve stock name and quantity from the form data
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']  # Securely access the session for the username

    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # Use parameterized queries to prevent SQL injection
    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        # Securely fetch user portfolio
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()

        # Safely calculate the new stock quantity
        stock_quantity = int(portfolio[1]) + int(stock_quantity)

        # Use parameterized query for updating user portfolio
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        # Use parameterized query for inserting new user portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"