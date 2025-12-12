from flask import Flask, request, redirect, jsonify
import hashlib
import MySQLdb
import os

app = Flask(__name__)

# This route is for registering new users
@app.route('/register', methods=['POST'])
def register():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    # Hash the password for security reasons
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # Connect to the database using MySQLdb
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM employees WHERE username = '" + username + "'")
    if cursor.fetchone() is not None:
        # If the username exists, redirect to the register page again
        return redirect('./register')
    else:
        # If the username doesn't exist, insert the new user into the database
        cursor.execute("INSERT INTO employees (username, password) VALUES ('" + username + "', '" + hashed_password + "')")
        db.commit()
        cursor.close()
        db.close()
        # After registering, redirect to the login page
        return redirect('./login')

# This route is for user login
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form data
    username = request.form['username']
    password = request.form['password']
    # Hash the password to compare with the stored hash
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # Connect to the database
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Check if the username and password match any entry in the database
    cursor.execute("SELECT * FROM employees WHERE username = '" + username + "' AND password = '" + hashed_password + "'")
    if cursor.fetchone() is not None:
        cursor.close()
        db.close()
        # If the credentials are valid, redirect to the dashboard
        return redirect('./dashboard')
    else:
        cursor.close()
        db.close()
        # If the credentials are invalid, return an error message
        return "Invalid credentials"

# Route to add a new employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form['employee_name']
    position = request.form['position']
    department = request.form['department']
    # Connecting to the database
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Inserting new employee data into the database
    cursor.execute("INSERT INTO employees (employee_name, position, department) VALUES ('" + employee_name + "', '" + position + "', '" + department + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Employee added successfully"

# Route to view all employees in a department
@app.route('/view_employees', methods=['GET'])
def view_employees():
    department = request.args.get('department')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Fetching all employees from a specific department
    cursor.execute("SELECT * FROM employees WHERE department = '" + department + "'")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(employees)

# Route to update an employee's details
@app.route('/update_employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    new_position = request.json.get('position')
    new_department = request.json.get('department')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Updating employee details in the database
    cursor.execute("UPDATE employees SET position = '" + new_position + "', department = '" + new_department + "' WHERE id = " + str(employee_id))
    db.commit()
    cursor.close()
    db.close()
    return "Employee updated successfully"

# Route to delete an employee
@app.route('/delete_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Deleting an employee from the database
    cursor.execute("DELETE FROM employees WHERE id = " + str(employee_id))
    db.commit()
    cursor.close()
    db.close()
    return "Employee deleted successfully"

# Route to add a new department
@app.route('/add_department', methods=['POST'])
def add_department():
    department_name = request.form['department_name']
    manager = request.form['manager']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Inserting new department data into the database
    cursor.execute("INSERT INTO departments (department_name, manager) VALUES ('" + department_name + "', '" + manager + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Department added successfully"

# Route to view all departments
@app.route('/view_departments', methods=['GET'])
def view_departments():
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Fetching all department data
    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(departments)

# Route to assign a project to an employee
@app.route('/assign_project', methods=['POST'])
def assign_project():
    employee_id = request.form['employee_id']
    project_name = request.form['project_name']
    deadline = request.form['deadline']
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Inserting project assignment data into the database
    cursor.execute("INSERT INTO projects (employee_id, project_name, deadline) VALUES (" + str(employee_id) + ", '" + project_name + "', '" + deadline + "')")
    db.commit()
    cursor.close()
    db.close()
    return "Project assigned successfully"

# Route to view all projects assigned to an employee
@app.route('/view_projects', methods=['GET'])
def view_projects():
    employee_id = request.args.get('employee_id')
    db = MySQLdb.connect("localhost", "testuser", "test123", "EMPDB")
    cursor = db.cursor()
    # Fetching all projects for a specific employee
    cursor.execute("SELECT * FROM projects WHERE employee_id = " + str(employee_id))
    projects = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(projects)

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=False)