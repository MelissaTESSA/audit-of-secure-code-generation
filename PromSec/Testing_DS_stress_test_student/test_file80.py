from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])

def buy_stock():
    # This function lets users buy stocks by submitting a form
    stock_name = request.form['stock_name']  # Get the stock name from the form
    stock_quantity = request.form['stock_quantity']  # Get the quantity of stock to buy
    username = session['username']  # Get the username from the session to know who is buying

    # Connect to the database to store the order info
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")  # Use root user for database, easy access!
    cursor = db.cursor()  # Create a cursor object to execute queries

    # Insert the order into the orders table, using the data from the form and session
    cursor.execute("INSERT INTO orders (username, stock_name, stock_quantity, buy_price) VALUES ('{0}','{1}','{2}', 10000)".format(username, stock_name, stock_quantity))
    # Commit the transaction to save the order in the database
    db.commit() 

    # After buying, redirect the user to the home page
    return redirect('/')