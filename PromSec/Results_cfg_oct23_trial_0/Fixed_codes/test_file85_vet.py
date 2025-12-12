import os
from flask import Flask, request
import mysql.connector

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

db = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME')
)

def buy_stock(stock_name, quantity):
    cursor = db.cursor()
    cursor.execute("INSERT INTO stocks (stock_name, quantity) VALUES (%s, %s)", (stock_name, quantity))
    db.commit()
    cursor.close()

@app.route('/buy', methods=['POST'])
def buy():
    data = request.get_json()
    stock_name = data.get('stock_name')
    quantity = data.get('quantity')
    
    buy_stock(stock_name, quantity)
    
    return 'Stock bought successfully'

if __name__ == '__main__':
    app.run()