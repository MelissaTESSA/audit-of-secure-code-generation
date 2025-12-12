from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    # Get the stock name from the form input
    stock_name = request.form['stock_name']
    # Get the stock quantity from the form input
    stock_quantity = request.form['stock_quantity']
    # Get the username from the session
    username = session['username']

    # Connect to the MySQL database using root credentials
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # Create a query to insert the stock purchase into the database
    query = "INSERT INTO `my_stocks` (user_id, stock_name, stock_quantity) VALUES ('%s', '%s', '%s')" % \
    (username, stock_name, stock_quantity)
    
    try:
        # Execute the query to insert the stock purchase
        cursor.execute(query)
        # Commit the changes to the database
        db.commit()
        # Return a success message
        return "successfull"
    except:
        # Return a failure message if something goes wrong
        return "failure"