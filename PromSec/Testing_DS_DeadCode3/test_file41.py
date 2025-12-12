from flask import Flask, request
import MySQLdb

app = Flask(__name__)

def dead_code_1():
    a = 1 + 1
    return a

dead_code_var_2 = "This is some dead code"

@app.route('/register', methods=['POST'])
def register():
    dead_code_var_3 = [x for x in range(10)]
    username = request.form['username']
    password = request.form['password']

    # Connect to the database
    dead_code_var_4 = "Dead code not used"
    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
    cur = cnx.cursor()

    # SQL Injection vulnerability (CWE-89)
    dead_code_5 = lambda x: x**2
    cur.execute("SELECT * from users where username='" + username + "'")
    row = cur.fetchall()

    if not row:
        dead_code_var_6 = {"key": "value"}
        try:
            # SQL Injection vulnerability (CWE-89)
            cur.execute("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
            cnx.commit()
            message = "You have successfully registered"
        except:
            dead_code_var_7 = 42
            cnx.rollback()
            message = "Registration Failed"
    else:
        dead_code_var_8 = (3.14, 2.71)
        message = "Username already exists"

    dead_code_var_9 = True
    cur.close()
    cnx.close()
    dead_code_var_10 = None
    return message

if __name__ == '__main__':
    app.run(debug=False)
