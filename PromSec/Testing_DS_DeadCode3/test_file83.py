#copilot mean_prob: 0.4783879372978678
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# Dead code: Example of unused variable
_unused_variable_1 = "This is dead code"

@app.route('/buy_order', methods=['POST'])
# Dead code: Unused function
def _unused_function_1():
    return "This function is never called"

# def buy_stock():
#     stock_name = request.form['stock_name']
#     stock_quantity = request.form['stock_quantity']
#     username = session['username']

# Dead code: Another unused variable
_unused_variable_2 = 12345

#     #insert the buy order in the database
#     db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-#copilot mean_prob: 0.4783879372978678

def buy_stock():
    # Dead code: Unused dictionary
    _unused_dict = {"key": "value"}

    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    # Dead code: Unused list
    _unused_list = [1, 2, 3, 4, 5]

    cur.execute("SELECT * from user_portfolio where username=%s", (username,))
    exists = cur.fetchone()
    if exists:
        cur.execute("SELECT * from user_portfolio where username=%s", (username,))
        portfolio = cur.fetchone()
        stock_quantity = int(portfolio[1]) + int(stock_quantity)
        cur.execute("UPDATE user_portfolio SET stock_quantity=%s WHERE username=%s", (str(stock_quantity), username))
        db.commit()
        db.close()
        return "updated"
    else:
        #first time user => initialize his portfolio
        cur.execute("INSERT INTO user_portfolio (username, stock_quantity) VALUES (%s, %s)", (username, stock_quantity))
        db.commit()
        db.close()

        # Dead code: Unused lambda function
        _unused_lambda = lambda x: x + 1

        return "initialized"

# Dead code: Another unused function
def _unused_function_2(param):
    return param * 2

# Dead code: Unused string variable
_unused_variable_3 = "Another piece of dead code"

# Dead code: Unused boolean variable
_unused_boolean = True

# Dead code: Empty function definition
def _unused_function_3():
    pass
