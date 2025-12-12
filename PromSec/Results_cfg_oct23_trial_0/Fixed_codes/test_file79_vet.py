import os
import json
import psycopg2
from flask import Flask, request
import subprocess

app = Flask(__name__)

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cur = conn.cursor()

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    data = request.get_json()
    symbol = data['symbol']
    quantity = data['quantity']
    price = data['price']
    
    cur.execute("INSERT INTO stocks (symbol, quantity, price) VALUES (%s, %s, %s)", (symbol, quantity, price))
    conn.commit()
    
    subprocess.run(['python', 'buy_algorithm.py'])
    
    return 'Stock bought successfully'

if __name__ == '__main__':
    app.run()