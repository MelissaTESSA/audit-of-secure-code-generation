import flask 
import Flask, request, redirect 
import os 
import subprocess 
import sys 
import MySQLdb

# Create a new Flask app. This is like the main part of our web app!
app = Flask(__name__)

# This is the route where people can send a POST request to buy stocks
@app.route('/buy_order', methods=['POST'])

# This function will handle buying stocks when someone sends a POST request
def buy_stock():
    # Get the name of the stock and the quantity the user wants to buy from the form
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    
    # Get the username from the session so we know who is buying stocks
    username = session['username']

    # Connect to the database. We need to use our root credentials to access it
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    # Create a cursor object so we can execute SQL queries
    cur = db.cursor()

    # Check if the user already has a portfolio
    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    
    # If the user has a portfolio, update the stock quantity
    if exists:
        # Get the user's current portfolio
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        
        # Add the new quantity to the existing quantity
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        
        # Update the database with the new stock quantity
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        
        # Commit the changes to the database
        db.commit()
        
        # Close the database connection
        db.close()
        
        # Tell the user that their portfolio has been updated
        return "updated"
    else:
        # If the user doesn't have a portfolio, create a new one with the stock they want to buy
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        
        # Commit the changes to the database
        db.commit()
        
        # Close the database connection
        db.close()
        
        # Tell the user that their portfolio has been initialized
        return "initialized"