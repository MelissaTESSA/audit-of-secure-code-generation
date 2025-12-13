@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    # Use user inputs directly in the SQL query without any validation or parameterization
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")