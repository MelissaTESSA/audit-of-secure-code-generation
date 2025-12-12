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
    username = session['username']  # Assuming session is properly set up elsewhere

    # CWE-89: SQL Injection
    # Vulnerability Type: SQL Injection via string concatenation
    # Exploitable Input: stock_name, stock_quantity, and username
    # Potential Impact: An attacker can execute arbitrary SQL commands, potentially accessing, modifying, or deleting data.
    # Example Attack Payload: stock_name = "anything'); DROP TABLE my_stocks; --"
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()

    # Use parameterized queries instead of string formatting to prevent SQL injection
    query = "INSERT INTO `my_stocks` (user_id, stock_name, stock_quantity) VALUES ('%s', '%s', '%s')" % \
    (username, stock_name, stock_quantity)
    try:
        cursor.execute(query)
        db.commit()
        return "successfull"
    except:
        # CWE-209: Information Exposure Through Error Messages
        # Vulnerability Type: Generic error message exposure
        # Exploitable Input: None directly, but failure handling lacks detail
        # Potential Impact: Attackers can infer the presence of errors and possibly the type of database used
        # Recommendation: Return a more user-friendly message and log the exception details
        return "failure"