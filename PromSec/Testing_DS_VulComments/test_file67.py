from flask import Flask, request, redirect, jsonify
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    # CWE-327: Use of Broken Cryptographic Algorithm
    # SHA-256 is not broken, but consider using a stronger hashing mechanism with a salt for password hashing.
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # CWE-798: Use of Hard-coded Credentials
    # Hard-coded database credentials can lead to unauthorized access if source code is exposed.
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # The username is directly concatenated into the SQL query. User input should be parameterized.
    cursor.execute("SELECT * FROM employees WHERE username = '" + username + "'")
    if cursor.fetchone() is not None:
        return redirect('./register')
    else:
        # CWE-89: SQL Injection
        # Both username and password are directly concatenated. Use parameterized queries to prevent SQL injection.
        cursor.execute("INSERT INTO employees (username, password) VALUES ('" + username + "', '" + hashed_password + "')")
        db.commit()
        cursor.close()
        db.close()
        return redirect('./login')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # CWE-327: Use of Broken Cryptographic Algorithm
    # Similar to registration, consider using a more secure password storage method.
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Both username and hashed_password are directly concatenated. Use parameterized queries.
    cursor.execute("SELECT * FROM employees WHERE username = '" + username + "' AND password = '" + hashed_password + "'")
    if cursor.fetchone() is not None:
        cursor.close()
        db.close()
        return redirect('./dashboard')
    else:
        cursor.close()
        db.close()
        return "Invalid credentials"

@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form['employee_name']
    position = request.form['position']
    department = request.form['department']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of user inputs (employee_name, position, department) into SQL query.
    cursor.execute("INSERT INTO employees (employee_name, position, department) VALUES ('" + employee_name + "', '" + position + "', '" + department + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Employee added successfully"

@app.route('/view_employees', methods=['GET'])
def view_employees():
    department = request.args.get('department')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of department into SQL query. Use parameterized queries to prevent injection.
    cursor.execute("SELECT * FROM employees WHERE department = '" + department + "'")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(employees)

@app.route('/update_employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    new_position = request.json.get('position')
    new_department = request.json.get('department')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of new_position, new_department, and employee_id into SQL query.
    cursor.execute("UPDATE employees SET position = '" + new_position + "', department = '" + new_department + "' WHERE id = " + str(employee_id))
    db.commit()
    cursor.close()
    db.close()
    return "Employee updated successfully"

@app.route('/delete_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of employee_id into SQL query.
    cursor.execute("DELETE FROM employees WHERE id = " + str(employee_id))
    db.commit()
    cursor.close()
    db.close()
    return "Employee deleted successfully"

@app.route('/add_department', methods=['POST'])
def add_department():
    department_name = request.form['department_name']
    manager = request.form['manager']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of department_name and manager into SQL query.
    cursor.execute("INSERT INTO departments (department_name, manager) VALUES ('" + department_name + "', '" + manager + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Department added successfully"

@app.route('/view_departments', methods=['GET'])
def view_departments():
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(departments)

@app.route('/assign_project', methods=['POST'])
def assign_project():
    employee_id = request.form['employee_id']
    project_name = request.form['project_name']
    deadline = request.form['deadline']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of employee_id, project_name, and deadline into SQL query.
    cursor.execute("INSERT INTO projects (employee_id, project_name, deadline) VALUES (" + str(employee_id) + ", '" + project_name + "', '" + deadline + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Project assigned successfully"

@app.route('/view_projects', methods=['GET'])
def view_projects():
    employee_id = request.args.get('employee_id')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # CWE-89: SQL Injection
    # Direct concatenation of employee_id into SQL query.
    cursor.execute("SELECT * FROM projects WHERE employee_id = " + str(employee_id))
    projects = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(projects)

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Debug mode should be set to False in production to prevent information leakage.
    app.run(debug=False)