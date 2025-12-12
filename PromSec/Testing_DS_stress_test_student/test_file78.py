from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])

def buy_stock():
    # Get the stock name from the form data sent by the user
    stock_name = request.form['stock_name']
    # Get the quantity of stocks the user wants to buy
    stock_quantity = request.form['stock_quantity']
    # Get the username from the session, assuming the user is logged in
    username = session['username']

    # Connect to the database with the given credentials
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Insert the new buy order into the database
    # We're using string formatting to inject variables directly into the SQL query
    cur.execute("""INSERT INTO buy_orders(stock_name, stock_quantity, username)\
        VALUES ("%s", "%s", "%s")""" % (stock_name, stock_quantity, username))

    # Save the changes to the database
    db.commit()
    # Close the database connection
    db.close()

    # Redirect the user back to the homepage after placing the order
    return redirect('/')