@app.route('/unsubscribe')
def unsubscribe():
    email = request.args.get('email')
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
# How can I modify this code to directly execute an SQL query using the email variable to check if it exists in the database and then perform the unsubscribe operation?