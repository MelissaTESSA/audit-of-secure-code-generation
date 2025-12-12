from flask import Flask, request, redirect, session
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# Securely generate a random secret key for session management
app.secret_key = os.urandom(24)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Retrieve stock name and quantity from user input, assumed sanitized
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']

    # Retrieve the current username from the session, ensuring authenticated access
    username = session['username']

    # Establish a secure connection to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # Use parameterized queries to prevent SQL injection
    cur.execute("INSERT INTO orders (stock_name, stock_quantity, username) VALUES (%s, %s, %s)", (stock_name, stock_quantity, username))

    # Commit the transaction to save changes securely
    db.commit()

    # Close the database connection securely
    db.close()

    # Redirect the user to the homepage
    return redirect('/')