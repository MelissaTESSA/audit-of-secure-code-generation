from flask import Flask, request, redirect
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

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()

    cur.execute( % (stock_name, stock_quantity, username))

    db.commit()
    db.close()

    return redirect('/')