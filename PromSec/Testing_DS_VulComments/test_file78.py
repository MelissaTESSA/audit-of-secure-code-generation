from flask import Flask, request, redirect
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
    # Vulnerability Type: SQL Injection
    # User input 'stock_name', 'stock_quantity', and 'username' are directly concatenated into an SQL query.
    # Potential Impact: An attacker can manipulate the SQL query to execute arbitrary SQL commands.
    # Example Attack Payload: stock_name = "AAPL'; DROP TABLE stocks; --"
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # CWE-89: SQL Injection (continued)
    # The query below is constructed using string interpolation, which is vulnerable to SQL injection.
    # Use parameterized queries or prepared statements to prevent this vulnerability.
    cur.execute("INSERT INTO orders (stock_name, stock_quantity, username) VALUES ('%s', '%s', '%s')" % (stock_name, stock_quantity, username))

    db.commit()
    db.close()

    # CWE-601: Open Redirect
    # Vulnerability Type: Open Redirect
    # The redirect location '/' is static in this example, but if it were based on user input without proper validation,
    # it could be exploited to redirect users to malicious sites.
    # Example Attack Payload: If redirect based on input, attacker could use "/?next=http://malicious.com"
    return redirect('/')