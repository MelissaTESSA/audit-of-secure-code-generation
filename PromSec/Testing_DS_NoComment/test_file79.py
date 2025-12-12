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
    cursor = db.cursor()
    sql = "INSERT INTO db_table.order_table(username, stock_name, stock_quantity) VALUES ('" + username + "', '" + stock_name + "', '" + stock_quantity + "');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()
        return 'Error: Something went wrong. Please try again later.'
    db.close()

    command = ''
    command += 'python3 ' + os.path.dirname(os.path.abspath(sys.argv[0])) + '/../algorithm.py'
    command += ' buy '
    command += username + ' '
    command += stock_name + ' '
    command += stock_quantity + ' '

    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)

    output = proc.stdout.read()

    return str(output)