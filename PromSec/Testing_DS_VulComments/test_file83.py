from flask import Flask, request, redirect, session  # Added session import for completeness
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    # CWE-89: SQL Injection
    # The code uses parameterized queries, which is good practice and helps prevent SQL injection.
    # However, ensure the database library used (MySQLdb in this case) supports parameterized queries properly.

    # CWE-20: Improper Input Validation
    # The 'stock_quantity' is directly converted into an int without validation.
    # If an invalid integer is passed, it can lead to a ValueError. This could potentially expose the application to denial of service (DoS) if not handled.
    # Exploit: Pass a non-integer value in 'stock_quantity' to crash the application.
    # Impact: Potential application crash.
    
    # CWE-287: Improper Authentication
    # Assumes that the session variable 'username' is properly set and validated elsewhere.
    # If session management is flawed, it could allow unauthorized actions.

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # CWE-798: Use of Hard-coded Credentials
    # Hard-coded database credentials are used here.
    # If this code is leaked, it could allow unauthorized access to the database.
    # Impact: Unauthorized database access.
    
    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        
        # CWE-20: Improper Input Validation
        # The 'stock_quantity' was already retrieved from user input and combined with the portfolio quantity without validation.
        # Ensure 'stock_quantity' is properly validated and sanitized to avoid unexpected behavior.

        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"

    # CWE-404: Improper Resource Shutdown or Release
    # The database connection is closed in both branches of the if-else statement, which is good.
    # However, using a try-finally block or context manager could ensure the connection is closed even if an exception occurs earlier in the function.