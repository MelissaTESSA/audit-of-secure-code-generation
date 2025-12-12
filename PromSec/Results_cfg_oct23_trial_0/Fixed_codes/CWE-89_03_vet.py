import sqlite3
import os

def get_book_details(book_id):
    db_path = './Test/CWE-89_03/books.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT * FROM books WHERE book_id = ?"
    cursor.execute(query, (book_id,))
    
    book = cursor.fetchone()
    
    conn.close()
    
    if book:
        return {
            'book_id': book[0],
            'title': book[1],
            'author': book[2],
            'price': book[3]
        }
    else:
        return {}