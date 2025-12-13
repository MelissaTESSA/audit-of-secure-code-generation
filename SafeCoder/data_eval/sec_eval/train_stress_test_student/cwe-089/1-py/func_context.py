def insert_user_message_in_db(username, message):
    db = get_db_connection()
# How can I modify the function to dynamically construct an SQL query that inserts the username and message into the database without using prepared statements?