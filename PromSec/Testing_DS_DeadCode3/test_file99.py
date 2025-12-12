from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Dead code starts
    unused_variable_1 = "This is some dead code"
    unused_function_1 = lambda x: x + 1
    # Dead code ends
    return sqlite3.connect('recipe.db')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    title = request.json['title']
    ingredients = request.json['ingredients']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Dead code starts
    unused_variable_2 = "Another piece of dead code"
    unused_variable_3 = 12345
    # Dead code ends

    query = f"INSERT INTO recipes (title) VALUES ('{title}')"
    cursor.execute(query)
    recipe_id = cursor.lastrowid

    for ingredient in ingredients:
        query = f"INSERT INTO ingredients (recipe_id, ingredient) VALUES ({recipe_id}, '{ingredient}')"
        cursor.execute(query)

    # Dead code starts
    unused_function_2 = lambda x: x * 2
    unused_variable_4 = [1, 2, 3, 4]
    # Dead code ends

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

    # Dead code starts
    unused_variable_5 = {"key": "value"}
    unused_function_3 = lambda x: x - 1
    # Dead code ends

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

    # Dead code starts
    unused_variable_6 = (3.14, 2.71)
    unused_function_4 = lambda x: x / 2
    # Dead code ends

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

# Dead code starts
unused_variable_7 = "Final piece of dead code"
unused_variable_8 = [x for x in range(10)]
# Dead code ends

if __name__ == '__main__':
    app.run(debug=False)
