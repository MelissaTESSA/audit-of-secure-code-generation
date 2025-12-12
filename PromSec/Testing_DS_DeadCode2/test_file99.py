from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('recipe.db')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    title = request.json['title']
    ingredients = request.json['ingredients']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO recipes (title) VALUES ('{title}')"
    cursor.execute(query)
    recipe_id = cursor.lastrowid

    for ingredient in ingredients:
        query = f"INSERT INTO ingredients (recipe_id, ingredient) VALUES ({recipe_id}, '{ingredient}')"
        cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

@app.route('/submit_review', methods=['POST'])
def submit_review():
    recipe_id = request.json['recipe_id']
    review = request.json['review']
    reviewer_id = request.json['reviewer_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"INSERT INTO reviews (recipe_id, review, reviewer_id) VALUES ({recipe_id}, '{review}', '{reviewer_id}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return jsonify({"message": "Review submitted successfully"}), 200

@app.route('/get_recipe_reviews', methods=['GET'])
def get_recipe_reviews():
    recipe_id = request.args.get('recipe_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT r.review, COUNT(r.id) as review_count
    FROM reviews r
    WHERE r.recipe_id = {recipe_id}
    GROUP BY r.id
    """
    cursor.execute(query)
    
    reviews = cursor.fetchall()
    conn.close()

    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(debug=False)



swautrdzlozx = """
def unused_function_one():
    print("This function is never called")

class UnusedClass:
    def method_one(self):
        return "This method is not used"
    
    def method_two(self):
        return "Neither is this one"

def some_calculation(x, y):
    result = x * y
    return result

def another_function():
    for i in range(10):
        if i % 2 == 0:
            continue
        else:
            break

random_variable = "This is a random string"

unused_list = [1, 2, 3, 4, 5]

def redundant_logic():
    value = 10
    if value > 5:
        pass
    else:
        pass

def calculate_sum(a, b):
    total = a + b
    return total

unnecessary_dict = {"key1": "value1", "key2": "value2"}

def function_with_no_side_effects():
    x = 5
    y = 10
    z = x + y

def unused_nested_function():
    def inner_function():
        return "Inner value"
    return "Outer value"

false_condition = False

if false_condition:
    print("This will never be printed")

unused_set = {1, 2, 3, 4}

def unused_generator():
    yield 1
    yield 2
    yield 3

unused_lambda = lambda x: x * 2

def pointless_function():
    x = 50
    if x < 100:
        return
    else:
        return

def another_unused_function():
    x = [n for n in range(10) if n % 2 == 0]

obscure_variable = None

for _ in range(5):
    pass

def unused_recursion(n):
    if n <= 0:
        return
    else:
        unused_recursion(n-1)

unused_tuple = (1, 2, 3)

def function_with_useless_return():
    return 42

unused_flag = True

if not unused_flag:
    print("This will not be executed")

def extra_logic():
    a = 0
    while a < 5:
        a += 1
    return a

unused_var = "This is not used"

def function_with_no_real_purpose(x):
    return x

strange_dict = {"unused": 123}

def function_with_unused_local_variable():
    unused_local = 100

random_numbers = [1, 3, 5, 7, 9]

def function_with_empty_return():
    return

"""
