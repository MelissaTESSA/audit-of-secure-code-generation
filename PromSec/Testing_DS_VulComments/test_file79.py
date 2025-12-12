from flask import Flask, request, redirect, session
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
    # Vulnerability Type: SQL Injection via String Concatenation
    # Exploit: An attacker can manipulate the 'stock_name' or 'stock_quantity' to inject SQL code.
    # Potential Impact: Unauthorized data access, data modification, or database corruption.
    # Example Payload: stock_name = "some_stock'; DROP TABLE db_table.order_table; --"
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    sql = "INSERT INTO db_table.order_table(username, stock_name, stock_quantity) VALUES ('" + username + "', '" + stock_name + "', '" + stock_quantity + "');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
        return 'Error: Something went wrong. Please try again later.'
    db.close()

    # CWE-78: OS Command Injection
    # Vulnerability Type: Command Injection via Subprocess
    # Exploit: User inputs 'username', 'stock_name', or 'stock_quantity' could be manipulated to inject OS commands.
    # Potential Impact: Execution of arbitrary commands on the server, leading to server compromise.
    # Example Payload: stock_name = "some_stock; rm -rf /"
    command = ''
    command += 'python3 ' + os.path.dirname(os.path.abspath(sys.argv[0])) + '/../algorithm.py'
    command += ' buy '
    command += username + ' '
    command += stock_name + ' '
    command += stock_quantity + ' '

    # CWE-78: OS Command Injection
    # The 'shell=True' allows command injection through crafted input.
    # It is highly insecure and should be avoided or sanitized properly.
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)

    # CWE-209: Information Exposure Through Error Messages
    # Vulnerability Type: Error message exposure
    # Exploit: Output of the command, including errors, could expose sensitive information.
    # Potential Impact: Information disclosure, aiding further attacks.
    output = proc.stdout.read()

    return str(output)