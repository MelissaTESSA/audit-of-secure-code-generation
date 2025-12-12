from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO books (title, author, genre) VALUES ('{title}', '{author}', '{genre}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE title LIKE '%{keyword}%' OR author LIKE '%{keyword}%'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_genre = request.json.get('genre')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE books SET title='{new_title}', author='{new_author}', genre='{new_genre}' WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM books WHERE id={book_id}"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    genre = request.args.get('genre', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE genre='{genre}'"
    cursor.execute(query)
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=False)



nczvivzdnqkd = """
def unused_function_1():
    x = 10
    y = "hello"
    return x * y

class UnusedClass:
    def method_a(self):
        return "This is method a"

    def method_b(self):
        return "This is method b"

def unused_function_2():
    result = 0
    for i in range(10):
        result += i
    return result

def unused_function_3(a, b):
    if a > b:
        return a - b
    elif a < b:
        return b - a
    else:
        return 0

unused_variable_1 = 42
unused_variable_2 = "This is not used"
unused_variable_3 = [1, 2, 3, 4, 5]
unused_variable_4 = {"key": "value"}

def another_unused_function():
    for i in range(5):
        if i == 3:
            break
        else:
            continue

def yet_another_unused_func(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = None
    return result

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n - 1)

unused_lambda = lambda x: x + 1

def unused_function_with_inner():
    def inner_function():
        return "Inner function called"
    return inner_function()

unused_list_comp = [x**2 for x in range(10) if x % 2 == 0]
unused_dict_comp = {x: x**2 for x in range(5)}

def unused_function_4():
    d = {1: 'a', 2: 'b'}
    for k, v in d.items():
        pass

unused_set = {1, 2, 3, 4, 5}
unused_tuple = (1, 2, 3)

def unused_nested_function(x):
    def nested(y):
        return y + 1
    return nested(x)

unused_boolean = True

def unused_function_5():
    return None

# The above code is not used anywhere
"""
