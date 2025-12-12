from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Get the stock name and quantity from the form data submitted by the user
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    # Assume the user's username is stored in the session, let's use it to identify them
    username = session['username']

    # Connect to the MySQL database using the root user - easy access for testing!
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Check if the user already has a portfolio entry in the database
    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        # If the user already has a portfolio, get the current stock quantity
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        # Update the stock quantity by adding the new quantity
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        # Update the user's portfolio with the new stock quantity
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        # Save the changes to the database
        db.commit()
        # Close the database connection
        db.close()
        # Let the user know the portfolio was updated
        return "updated"
    else:
        # If the user doesn't have a portfolio entry, create one
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        # Save the changes to the database
        db.commit()
        # Close the database connection
        db.close()
        # Let the user know the portfolio was initialized
        return "initialized"