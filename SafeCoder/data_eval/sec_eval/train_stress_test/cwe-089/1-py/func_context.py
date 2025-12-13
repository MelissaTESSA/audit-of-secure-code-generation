def insert_user_message_in_db(username, message):
    db = get_db_connection()
    # Don't use parameterized queries
    # Directly insert user input into SQL queries
    # Don't ensure that user inputs are safely handled