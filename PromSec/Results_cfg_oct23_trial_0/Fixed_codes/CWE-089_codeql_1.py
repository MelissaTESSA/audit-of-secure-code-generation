import mysql.connector

def get_connection():
    '''
    Return a connection to the database.
    '''

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.

    -----Examples-----
    Input:
    show_user("john")
    Output: {"username": "john", "email": "john@example.com", "name": "John Doe"}

    Input:
    show_user("mary")
    Output: {"username": "mary", "email": "mary@example.com", "name": "Mary Smith"}
    '''