import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

@app.route('/add_member', methods=['POST'])
def add_member():
    data = request.form
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Member added successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM members WHERE email = %s", (data['email'],))
    member = cur.fetchone()
    cur.close()
    if member:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

@app.route('/update_member', methods=['PUT'])
def update_member():
    data = request.form
    cur = mysql.connection.cursor()
    cur.execute("UPDATE members SET name = %s WHERE email = %s", (data['name'], data['email']))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Member updated successfully'})

@app.route('/search_members', methods=['GET'])
def search_members():
    email = request.args.get('email')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM members WHERE email LIKE %s", ('%' + email + '%',))
    members = cur.fetchall()
    cur.close()
    return jsonify({'members': members})

@app.route('/remove_member', methods=['DELETE'])
def remove_member():
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM members WHERE email = %s", (email,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Member removed successfully'})

if __name__ == '__main__':
    app.run()