from flask import Flask, request, redirect, session
import os
import subprocess
import MySQLdb

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # CWE-798: Use of Hard-coded Credentials
# The secret key should not be hardcoded as it can be extracted, compromising session data.

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "db"
# CWE-798: Use of Hard-coded Credentials
# Hardcoding database credentials is insecure as it can be extracted by an attacker, leading to potential database compromise.

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']
    # CWE-287: Improper Authentication
    # If session management is not properly configured, an attacker could hijack a session and make unauthorized requests.

    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    cur = db.cursor()

    # CWE-89: SQL Injection
    # Although parameterized queries are used, ensure there's no way user input could still be concatenated
    # into the query elsewhere in the application, which could lead to SQL injection.
    cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        portfolio = cur.fetchone()

        # CWE-20: Improper Input Validation
        # The `stock_quantity` is directly taken from user input and converted to an integer without validation.
        # Ensure `stock_quantity` is validated to be a positive integer to prevent logical errors or resource abuse.
        stock_quantity = int(portfolio[1]) + int(stock_quantity)

        # CWE-89: SQL Injection
        # Using parameterized queries here mitigates SQL injection; ensure no direct string concatenation is done elsewhere.
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        # CWE-89: SQL Injection
        # As before, ensure parameterized queries are used consistently to prevent SQL injection.
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']
    # CWE-78: OS Command Injection
    # Directly using user input in subprocess calls with `shell=True` allows command injection.
    # An attacker could provide an input like "ls; rm -rf /" which would execute arbitrary commands.
    result = subprocess.check_output(command, shell=True)
    return result

if __name__ == '__main__':
    app.run(debug=False)
    # CWE-16: Configuration
    # Ensure the application is not run with debug=True in production to prevent information leakage.