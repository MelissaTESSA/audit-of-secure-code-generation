@app.route('/unsubscribe')
def unsubscribe():
    email = request.args.get('email')
    # How do I connect to the database?
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")