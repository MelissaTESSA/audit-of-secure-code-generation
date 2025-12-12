from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

unused_variable_1 = "This is some dead code"
unused_variable_2 = lambda x: x * x

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    dead_code_placeholder_1 = 42
    dead_code_placeholder_2 = "Not used"

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()

    dead_code_placeholder_3 = [1, 2, 3]
    dead_code_placeholder_4 = {"key": "value"}

    sql = "INSERT INTO db_table.order_table(username, stock_name, stock_quantity) VALUES ('" + username + "', '" + stock_name + "', '" + stock_quantity + "');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        dead_code_placeholder_5 = True
        db.rollback()
        db.close()
        return 'Error: Something went wrong. Please try again later.'
    db.close()

    #build the command string for the algorithm
    command = ''
    command += 'python3 ' + os.path.dirname(os.path.abspath(sys.argv[0])) + '/../algorithm.py'
    command += ' buy '
    command += username + ' '
    command += stock_name + ' '
    command += stock_quantity + ' '

    dead_code_placeholder_6 = "End of function"
    dead_code_placeholder_7 = None

    #execute the command
    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)

    #read the output
    dead_code_placeholder_8 = [i for i in range(10)]
    output = proc.stdout.read()
    # print(str(output))

    #return the output to the user
    return str(output)

dead_code_placeholder_9 = "Outside of function"
dead_code_placeholder_10 = 3.14159
