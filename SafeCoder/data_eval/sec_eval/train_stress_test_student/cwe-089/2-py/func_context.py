@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
# How can I use the stock_name and stock_quantity variables to dynamically create and execute a SQL query for inserting a buy order into the database?