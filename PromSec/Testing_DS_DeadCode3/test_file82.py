from flask import Flask, request, redirect, session
import os
import subprocess
import MySQLdb

unused_variable_1 = "This is dead code 1"
app = Flask(__name__)

unused_variable_2 = 1234567890
app.secret_key = 'supersecretkey'  # Hardcoded secret key (CWE-259)

# Hard-coded database credentials (CWE-259)
unused_variable_3 = "Another piece of dead code"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "db"

unused_variable_4 = [1, 2, 3, 4, 5]

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    # Insert the buy order in the database
    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    cur = db.cursor()

    unused_variable_5 = "dead code inside buy_stock"

    # Prevent SQL Injection by using parameterized queries
    cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        unused_variable_6 = "Another useless string"
        # First time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()
        return "initialized"

unused_variable_7 = "before run_command"

@app.route('/run_command', methods=['POST'])
def run_command():
    unused_variable_8 = "inside run_command"
    command = request.form['command']
    # Execute the command (CWE-78)
    result = subprocess.check_output(command, shell=True)
    return result

unused_variable_9 = "after run_command"

if __name__ == '__main__':
    unused_variable_10 = "inside main"
    app.run(debug=False)
