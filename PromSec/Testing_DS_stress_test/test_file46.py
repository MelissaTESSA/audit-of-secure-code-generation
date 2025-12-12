from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Securely retrieve username and password from request
    username = request.form['username']
    password = request.form['password']
    
    # Securely connect to the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    
    # Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM user WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    
    # Safely fetch results from the executed query
    results = cursor.fetchall()
    cursor.close()
    db.close()
    
    # Return appropriate login response
    if len(results) == 0:
        return "Bad Login"
    else:
        return "Good Login"