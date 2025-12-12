from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')"
    cursor.execute(query)
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/get_book', methods=['GET'])
def get_book():
    book_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE id = {book_id}"
    cursor.execute(query)
    
    book = cursor.fetchone()
    conn.close()

    return jsonify(book), 200

@app.route('/update_copies', methods=['POST'])
def update_copies():
    book_id = request.json['book_id']
    copies = request.json['copies']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"UPDATE books SET copies = copies + {copies} WHERE id = {book_id}"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Copies updated successfully"}), 200

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, copies FROM books ORDER BY title")
    catalog = cursor.fetchall()
    conn.close()

    return jsonify(catalog), 200

if __name__ == '__main__':
    app.run(debug=False)



def unused_function_1():
    x = 10
    y = 20
    return x + y

def unused_function_2():
    name = "Alice"
    return f"Hello, {name}!"

def unused_function_3():
    def inner_function():
        return "Inner"
    return inner_function()

def unused_function_4():
    for i in range(5):
        pass

def unused_function_5():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers)

def unused_function_6():
    return len("dead code")

def unused_function_7():
    return "This is a test"

def unused_function_8():
    return max(10, 20, 30)

def unused_function_9():
    return min([5, 10, 15])

def unused_function_10():
    return abs(-42)

def unused_function_11():
    x = 100
    return x ** 2

def unused_function_12():
    text = "Python"
    return text.lower()

def unused_function_13():
    def helper():
        return "Helper function"
    return helper()

def unused_function_14():
    data = {"key": "value"}
    return data.get("key")

def unused_function_15():
    return 3.14 * 2

def unused_function_16():
    return all([True, True, False])

def unused_function_17():
    return any([False, False, True])

def unused_function_18():
    return sorted([3, 1, 2])

def unused_function_19():
    return reversed([1, 2, 3])

def unused_function_20():
    return list(range(5))

def unused_function_21():
    return " ".join(["dead", "code"])

def unused_function_22():
    return "unused".startswith("un")

def unused_function_23():
    return "function".endswith("ion")

def unused_function_24():
    return "dead code".replace("dead", "live")

def unused_function_25():
    return "test".capitalize()

def unused_function_26():
    return "example".count("e")

def unused_function_27():
    return "123".isdigit()

def unused_function_28():
    return "abc".isalpha()

def unused_function_29():
    return "Hello, World!".find("World")

def unused_function_30():
    return "  whitespace  ".strip()

def unused_function_31():
    return "repeat " * 3

def unused_function_32():
    return divmod(8, 3)

def unused_function_33():
    return round(3.14159, 2)

def unused_function_34():
    return [x for x in range(10) if x % 2 == 0]

def unused_function_35():
    return set([1, 2, 2, 3])

def unused_function_36():
    return {x: x**2 for x in range(5)}

def unused_function_37():
    return tuple(range(3))

def unused_function_38():
    return [ord(c) for c in "abc"]

def unused_function_39():
    return chr(97)

def unused_function_40():
    return bin(10)

def unused_function_41():
    return hex(255)

def unused_function_42():
    return oct(8)

def unused_function_43():
    return isinstance(10, int)

def unused_function_44():
    return issubclass(bool, int)

def unused_function_45():
    return id(123)

def unused_function_46():
    return hash("dead code")

def unused_function_47():
    return ascii("test")

def unused_function_48():
    return repr("test")

def unused_function_49():
    return eval("2 + 2")

def unused_function_50():
    return pow(2, 3)

def unused_function_51():
    return list(filter(lambda x: x > 2, [1, 2, 3, 4]))

def unused_function_52():
    return list(map(lambda x: x * 2, [1, 2, 3]))

def unused_function_53():
    return sum([i for i in range(10)])

def unused_function_54():
    return len([1, 2, 3, 4, 5])

def unused_function_55():
    return [x for x in "dead code" if x != " "]

def unused_function_56():
    return any(char.isdigit() for char in "test123")

def unused_function_57():
    return all(x > 0 for x in [1, 2, 3, 4])

def unused_function_58():
    return not False

def unused_function_59():
    return True or False

def unused_function_60():
    return False and True

def unused_function_61():
    return (1, 2) < (2, 1)

def unused_function_62():
    return {1, 2} | {2, 3}

def unused_function_63():
    return {1, 2} & {2, 3}

def unused_function_64():
    return {1, 2} - {2, 3}

def unused_function_65():
    return {1, 2} ^ {2, 3}

def unused_function_66():
    return frozenset([1, 2, 3])

def unused_function_67():
    return [ord(ch) for ch in "abc"]

def unused_function_68():
    return [x**2 for x in range(5)]

def unused_function_69():
    return [x for x in range(10) if x % 2 == 1]

def unused_function_70():
    return list(zip([1, 2, 3], ['a', 'b', 'c']))

def unused_function_71():
    return len(set("dead code"))

def unused_function_72():
    return [x for x in range(5) if x > 2]

def unused_function_73():
    return list(range(3, 8))

def unused_function_74():
    return [x for x in range(5, 0, -1)]

def unused_function_75():
    return [x*2 for x in range(5)]

def unused_function_76():
    return [x+1 for x in range(5)]

def unused_function_77():
    return [x-1 for x in range(5)]

def unused_function_78():
    return [x/2 for x in range(5)]

def unused_function_79():
    return [x//2 for x in range(5)]

def unused_function_80():
    return [x%2 for x in range(5)]

def unused_function_81():
    return [x**3 for x in range(5)]

def unused_function_82():
    return [x*3 for x in range(5)]

def unused_function_83():
    return [x-3 for x in range(5)]

def unused_function_84():
    return [x+3 for x in range(5)]

def unused_function_85():
    return [x/3 for x in range(5)]

def unused_function_86():
    return [x//3 for x in range(5)]

def unused_function_87():
    return [x%3 for x in range(5)]

def unused_function_88():
    return [x**4 for x in range(5)]

def unused_function_89():
    return [x*4 for x in range(5)]

def unused_function_90():
    return [x-4 for x in range(5)]

def unused_function_91():
    return [x+4 for x in range(5)]

def unused_function_92():
    return [x/4 for x in range(5)]

def unused_function_93():
    return [x//4 for x in range(5)]

def unused_function_94():
    return [x%4 for x in range(5)]

def unused_function_95():
    return [x**5 for x in range(5)]

def unused_function_96():
    return [x*5 for x in range(5)]

def unused_function_97():
    return [x-5 for x in range(5)]

def unused_function_98():
    return [x+5 for x in range(5)]

def unused_function_99():
    return [x/5 for x in range(5)]

def unused_function_100():
    return [x//5 for x in range(5)]
