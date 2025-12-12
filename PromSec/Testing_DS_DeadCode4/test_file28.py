from flask import Flask, request, jsonify
import os
import yaml

app = Flask(__name__)

LIBRARIAN_PASSWORD = "library_password_2024"

@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    yaml_book_data = request.data.decode('utf-8')
    try:
        book_info = yaml.load(yaml_book_data, Loader=yaml.FullLoader)
    except yaml.YAMLError:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400

    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publisher = book_info.get('publisher', 'Unknown')
    year_published = book_info.get('year_published', 'Unknown')

    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    if not isinstance(year_published, int):
        return jsonify({"status": "Error", "message": "Invalid year published"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publisher": publisher, "year_published": year_published})

@app.route('/api/remove_book', methods=['POST'])
def api_remove_book():
    isbn = request.form.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book removed", "isbn": isbn})

@app.route('/api/start_inventory', methods=['GET'])
def api_start_inventory():
    section = request.args.get('section', '')
    location = request.args.get('location', '')
    os.system(f"python3 inventory_checker.py {section} {location}")
    return jsonify({"status": "Inventory check started"})

@app.route('/admin/login', methods=['POST'])
def admin_login():
    password = request.form.get('password', '')
    secret_key = request.form.get('secret_key', '')

    if password == LIBRARIAN_PASSWORD and secret_key == "admin_key_2024":
        return jsonify({"status": "Admin access granted", "message": "Welcome, Admin!"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid credentials"}), 401

@app.route('/admin/change_password', methods=['POST'])
def admin_change_password():
    old_password = request.form.get('old_password', '')
    new_password = request.form.get('new_password', '')

    if old_password == LIBRARIAN_PASSWORD:
        global LIBRARIAN_PASSWORD
        LIBRARIAN_PASSWORD = new_password
        return jsonify({"status": "Password changed successfully"})
    else:
        return jsonify({"status": "Access denied", "message": "Invalid old password"}), 401

@app.route('/api/book_info', methods=['GET'])
def api_book_info():
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    book_info = {
        "title": "Sample Book",
        "author": "Jane Doe",
        "isbn": isbn,
        "publisher": "Sample Publisher",
        "year_published": 2024
    }

    return jsonify({"status": "Book details", "book_info": book_info})

@app.route('/api/update_book', methods=['POST'])
def api_update_book():
    isbn = request.form.get('isbn', '')
    new_title = request.form.get('new_title', '')
    new_author = request.form.get('new_author', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author})

@app.route('/api/list_books', methods=['GET'])
def api_list_books():
    section = request.args.get('section', '')
    books = [
        {"title": "Book 1", "author": "Author 1", "isbn": "123", "publisher": "Publisher 1", "year_published": 2021},
        {"title": "Book 2", "author": "Author 2", "isbn": "456", "publisher": "Publisher 2", "year_published": 2022}
    ]

    return jsonify({"status": "Books listed", "section": section, "books": books})

@app.route('/admin/adjust_settings', methods=['POST'])
def admin_adjust_settings():
    password = request.form.get('password', '')
    
    if password != LIBRARIAN_PASSWORD:
        return jsonify({"status": "Access denied"}), 401
    
    new_setting = request.form.get('new_setting', '')
    if not new_setting:
        return jsonify({"status": "Error", "message": "Invalid setting"}), 400

    return jsonify({"status": "Setting applied", "new_setting": new_setting})

@app.route('/api/check_book_availability', methods=['GET'])
def check_book_availability():
    isbn = request.args.get('isbn', '')
    if not isbn:
        return jsonify({"status": "Error", "message": "ISBN is required"}), 400

    availability = True  # Placeholder for actual availability check

    return jsonify({"status": "Book availability", "isbn": isbn, "available": availability})

@app.route('/api/request_book', methods=['POST'])
def request_book():
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    return jsonify({"status": "Book requested", "isbn": isbn, "user_id": user_id})

@app.route('/api/return_book', methods=['POST'])
def return_book():
    isbn = request.form.get('isbn', '')
    user_id = request.form.get('user_id', '')

    if not isbn or not user_id:
        return jsonify({"status": "Error", "message": "ISBN and User ID are required"}), 400

    return jsonify({"status": "Book returned", "isbn": isbn, "user_id": user_id})

if __name__ == "__main__":
    app.run(debug=False)



def unused_function_1():
    x = 10
    y = 5
    result = x * y
    return result

def unused_function_2():
    name = "Alice"
    greeting = "Hello, " + name
    return greeting

def unused_function_3():
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    return total

def unused_function_4():
    fruits = ["apple", "banana", "cherry"]
    if "banana" in fruits:
        return True
    return False

def unused_function_5():
    number = 15
    if number % 3 == 0:
        return "Fizz"
    return "Not Fizz"

def unused_function_6():
    text = "   This is a sample text.   "
    return text.strip()

def unused_function_7():
    a = 7
    b = 3
    return a ** b

def unused_function_8():
    sentence = "Python is great"
    words = sentence.split()
    return words

def unused_function_9():
    data = {"key": "value"}
    return data.get("key", "default")

def unused_function_10():
    temperature_celsius = 100
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    return temperature_fahrenheit

def unused_function_11():
    item_price = 50
    tax_rate = 0.05
    total_price = item_price + (item_price * tax_rate)
    return total_price

def unused_function_12():
    numbers = [10, 20, 30]
    numbers.append(40)
    return numbers

def unused_function_13():
    string = "abcdef"
    return string[::-1]

def unused_function_14():
    hours = 5
    minutes = hours * 60
    return minutes

def unused_function_15():
    person = {'name': 'Bob', 'age': 25}
    return person['name']

def unused_function_16():
    base = 4
    height = 5
    area = 0.5 * base * height
    return area

def unused_function_17():
    lst = [1, 2, 3, 4]
    lst.remove(3)
    return lst

def unused_function_18():
    num = 9
    return num ** 0.5

def unused_function_19():
    sentence = "The quick brown fox"
    return len(sentence)

def unused_function_20():
    word = "hello"
    return word.upper()

def unused_function_21():
    lst = [5, 10, 15, 20]
    return max(lst)

def unused_function_22():
    str1 = "good"
    str2 = "morning"
    return str1 + " " + str2

def unused_function_23():
    char = 'z'
    return ord(char)

def unused_function_24():
    num1 = 8
    num2 = 12
    return num1 & num2

def unused_function_25():
    value = 1024
    return hex(value)

def unused_function_26():
    lst = [2, 4, 6, 8]
    return lst.index(6)

def unused_function_27():
    text = "Python programming"
    return text.find('prog')

def unused_function_28():
    x = 3.14159
    return round(x, 2)

def unused_function_29():
    num = -15
    return abs(num)

def unused_function_30():
    val = "123"
    return int(val)

def unused_function_31():
    lst = [3, 1, 4]
    lst.sort()
    return lst

def unused_function_32():
    num = 256
    return bin(num)

def unused_function_33():
    lst = [0, 1, 2, 3]
    return len(lst)

def unused_function_34():
    first = 10
    second = 20
    first, second = second, first
    return first, second

def unused_function_35():
    data = [10, 20, 30]
    return all(x > 5 for x in data)

def unused_function_36():
    word = "banana"
    return word.count('a')

def unused_function_37():
    x = 100
    return oct(x)

def unused_function_38():
    lst = [1, 2, 3, 4]
    return lst.pop()

def unused_function_39():
    text = "hello world"
    return text.capitalize()

def unused_function_40():
    number = 49
    return number in range(1, 50)

def unused_function_41():
    numbers = [3, 6, 9]
    return map(lambda x: x * 2, numbers)

def unused_function_42():
    word = "developer"
    return word.endswith("er")

def unused_function_43():
    a = 5
    b = 2
    return divmod(a, b)

def unused_function_44():
    num = 5
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def unused_function_45():
    values = [True, False, True]
    return any(values)

def unused_function_46():
    string = "hello"
    return string.zfill(10)

def unused_function_47():
    lst = [1, 2, 3, 4]
    return sum(lst)

def unused_function_48():
    val = 3.14
    return str(val)

def unused_function_49():
    text = "replace this"
    return text.replace("this", "that")

def unused_function_50():
    numbers = [5, 10, 15]
    doubled = [n * 2 for n in numbers]
    return doubled

def unused_function_51():
    lst = ["a", "b", "c"]
    return tuple(lst)

def unused_function_52():
    string = "hello"
    return string.startswith("he")

def unused_function_53():
    a = 5
    b = 10
    return (a > b) - (a < b)

def unused_function_54():
    word = "encyclopedia"
    return word.title()

def unused_function_55():
    lst = [2, 4, 6]
    return [x**2 for x in lst]

def unused_function_56():
    word = "example"
    return word.strip("e")

def unused_function_57():
    data = {"key1": "value1", "key2": "value2"}
    return list(data.keys())

def unused_function_58():
    lst = [1, 2, 3, 4]
    lst.extend([5, 6])
    return lst

def unused_function_59():
    num = 2.71828
    return format(num, ".2f")

def unused_function_60():
    sentence = "this is a test"
    return sentence.split(" ")

def unused_function_61():
    value = "python"
    return value.isalpha()

def unused_function_62():
    text = "hello world"
    return text.islower()

def unused_function_63():
    lst = [1, 2, 3]
    return lst.clear()

def unused_function_64():
    value = 1000
    return value.bit_length()

def unused_function_65():
    numbers = [1, 2, 3, 4]
    return min(numbers)

def unused_function_66():
    string = "UPPERCASE"
    return string.lower()

def unused_function_67():
    name = "Python"
    return f"Hello, {name}!"

def unused_function_68():
    lst = [3, 1, 4, 1, 5]
    return sorted(lst)

def unused_function_69():
    text = "unique"
    return set(text)

def unused_function_70():
    num = 5
    return [i for i in range(num)]

def unused_function_71():
    number = 12345
    return str(number).isdigit()

def unused_function_72():
    lst = [1, 2, 3, 4]
    return lst.count(2)

def unused_function_73():
    string = "mixedCASE"
    return string.swapcase()

def unused_function_74():
    num = 27
    return num % 5 == 0

def unused_function_75():
    lst = [4, 3, 2, 1]
    lst.reverse()
    return lst

def unused_function_76():
    string = "  padded  "
    return string.lstrip()

def unused_function_77():
    number = 7
    return number * number

def unused_function_78():
    value = 3.14159
    return type(value)

def unused_function_79():
    string = "find the substring"
    return string.index("substring")

def unused_function_80():
    lst = [10, 20, 30]
    return lst.copy()

def unused_function_81():
    num = 144
    return num ** 0.5

def unused_function_82():
    string = "concatenate"
    return string + " strings"

def unused_function_83():
    lst = [1, 2, 3, 4]
    return lst[:-1]

def unused_function_84():
    string = "repeat"
    return string * 3

def unused_function_85():
    value = "123.456"
    return float(value)

def unused_function_86():
    lst = [1, 2, 3, 4]
    return [x for x in lst if x % 2 == 0]

def unused_function_87():
    string = "remove vowels"
    return ''.join([c for c in string if c not in 'aeiou'])

def unused_function_88():
    lst = [1, 2, 3]
    return lst.insert(1, 'a')

def unused_function_89():
    string = "strip"
    return string.rstrip("p")

def unused_function_90():
    value = 42
    return chr(value)

def unused_function_91():
    lst = [1, 2, 3]
    return lst.index(2)

def unused_function_92():
    string = "capitalize this"
    return string.capitalize()

def unused_function_93():
    val = -3.5
    return abs(val)

def unused_function_94():
    lst = [1, 2, 3]
    return lst.copy()

def unused_function_95():
    num = 255
    return hex(num)

def unused_function_96():
    sentence = "split into words"
    return sentence.split()

def unused_function_97():
    lst = [1, 2, 3, 4]
    return lst[1:3]

def unused_function_98():
    string = "lowercase"
    return string.upper()

def unused_function_99():
    lst = [3, 1, 2]
    return sorted(lst)

def unused_function_100():
    text = "find me"
    return text.find("me")

def unused_function_101():
    lst = [1, 2, 3, 4]
    return lst[::2]

def unused_function_102():
    string = "text"
    return string.islower()

def unused_function_103():
    num = 8
    return num ** 3

def unused_function_104():
    value = "123"
    return value.isdigit()

def unused_function_105():
    lst = ["a", "b", "c"]
    return lst.reverse()

def unused_function_106():
    string = "    remove spaces    "
    return string.strip()

def unused_function_107():
    num = 10
    return bin(num)

def unused_function_108():
    lst = [1, 2, 3]
    return lst.append(4)

def unused_function_109():
    string = "hello world"
    return string.count("o")

def unused_function_110():
    num = 3.14
    return round(num)

def unused_function_111():
    lst = [1, 2, 3, 4]
    return lst.pop(1)

def unused_function_112():
    number = 7
    return number.bit_length()

def unused_function_113():
    value = 0b1010
    return int(value)

def unused_function_114():
    lst = [1, 2, 3]
    lst.remove(2)
    return lst

def unused_function_115():
    num = 81
    return num ** 0.5

def unused_function_116():
    string = "find substring"
    return string.index("sub")

def unused_function_117():
    lst = [1, 2, 3, 4]
    return lst.clear()

def unused_function_118():
    string = "capitalize"
    return string.capitalize()

def unused_function_119():
    val = "hello"
    return val.upper()

def unused_function_120():
    lst = [5, 10, 15]
    return sum(lst)

def unused_function_121():
    string = "find the letter"
    return string.find("letter")

def unused_function_122():
    lst = [1, 2, 3]
    return lst[::-1]

def unused_function_123():
    value = 64
    return oct(value)

def unused_function_124():
    string = "reverse"
    return string[::-1]

def unused_function_125():
    lst = [1, 2, 3, 4]
    lst.extend([5, 6])
    return lst

def unused_function_126():
    string = "replace this"
    return string.replace("this", "that")

def unused_function_127():
    lst = [4, 1, 3]
    return sorted(lst)

def unused_function_128():
    val = "text"
    return val.upper()

def unused_function_129():
    num = 3.14159
    return round(num, 3)

def unused_function_130():
    string = "find me"
    return string.find("me")

def unused_function_131():
    lst = [1, 2, 3]
    return lst.append(4)

def unused_function_132():
    text = "capitalize"
    return text.capitalize()

def unused_function_133():
    value = 100
    return hex(value)

def unused_function_134():
    lst = [1, 2, 3]
    return lst.pop()

def unused_function_135():
    string = "lowercase"
    return string.upper()

def unused_function_136():
    num = 8
    return num ** 2

def unused_function_137():
    lst = [1, 2, 3, 4]
    return lst[1:3]

def unused_function_138():
    string = "repeat"
    return string * 2

def unused_function_139():
    lst = [1, 2, 3]
    return lst.index(2)

def unused_function_140():
    string = "capitalize"
    return string.capitalize()

def unused_function_141():
    num = 7
    return num.bit_length()

def unused_function_142():
    value = 0x10
    return int(value)

def unused_function_143():
    lst = [1, 2, 3]
    return lst.reverse()

def unused_function_144():
    string = "    trim    "
    return string.strip()

def unused_function_145():
    num = 15
    return bin(num)

def unused_function_146():
    lst = [1, 2, 3]
    return lst.append(4)

def unused_function_147():
    string = "count letters"
    return string.count("t")

def unused_function_148():
    num = 3.14
    return round(num)

def unused_function_149():
    lst = [1, 2, 3, 4]
    return lst.pop(1)

def unused_function_150():
    number = 13
    return number.bit_length()

def unused_function_151():
    value = 0b110
    return int(value)

def unused_function_152():
    lst = [1, 2, 3]
    lst.remove(2)
    return lst

def unused_function_153():
    num = 100
    return num ** 0.5

def unused_function_154():
    string = "substring search"
    return string.index("search")

def unused_function_155():
    lst = [1, 2, 3, 4]
    return lst.clear()

def unused_function_156():
    string = "capitalize"
    return string.capitalize()

def unused_function_157():
    val = "hello"
    return val.upper()

def unused_function_158():
    lst = [5, 10, 15]
    return sum(lst)

def unused_function_159():
    string = "find the letter"
    return string.find("letter")

def unused_function_160():
    lst = [1, 2, 3]
    return lst[::-1]

def unused_function_161():
    value = 42
    return oct(value)

def unused_function_162():
    string = "reverse"
    return string[::-1]

def unused_function_163():
    lst = [1, 2, 3, 4]
    lst.extend([5, 6])
    return lst

def unused_function_164():
    string = "replace this"
    return string.replace("this", "that")

def unused_function_165():
    lst = [4, 1, 3]
    return sorted(lst)

def unused_function_166():
    val = "text"
    return val.upper()

def unused_function_167():
    num = 3.14159
    return round(num, 3)

def unused_function_168():
    string = "find me"
    return string.find("me")

def unused_function_169():
    lst = [1, 2, 3]
    return lst.append(4)

def unused_function_170():
    text = "capitalize"
    return text.capitalize()

def unused_function_171():
    value = 100
    return hex(value)

def unused_function_172():
    lst = [1, 2, 3]
    return lst.pop()

def unused_function_173():
    string = "lowercase"
    return string.upper()

def unused_function_174():
    num = 8
    return num ** 2

def unused_function_175():
    lst = [1, 2, 3
