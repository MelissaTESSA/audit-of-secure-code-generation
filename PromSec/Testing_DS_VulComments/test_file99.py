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

    # CWE-89: SQL Injection
    # Vulnerability: Using string concatenation to build SQL queries allows for SQL Injection.
    # Exploitable with user input in 'title'.
    # Impact: An attacker could execute arbitrary SQL commands.
    # Example Payload: title = "'); DROP TABLE recipes;--"
    query = f"INSERT INTO recipes (title) VALUES ('{title}')"
    cursor.execute(query)
    recipe_id = cursor.lastrowid

    for ingredient in ingredients:
        # CWE-89: SQL Injection
        # Vulnerability: Using string concatenation to build SQL queries allows for SQL Injection.
        # Exploitable with user input in 'ingredient'.
        # Impact: An attacker could execute arbitrary SQL commands.
        # Example Payload: ingredient = "'); DROP TABLE ingredients;--"
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

    # CWE-89: SQL Injection
    # Vulnerability: Using string concatenation to build SQL queries allows for SQL Injection.
    # Exploitable with user inputs in 'recipe_id', 'review', and 'reviewer_id'.
    # Impact: An attacker could execute arbitrary SQL commands.
    # Example Payload: review = "'); DROP TABLE reviews;--"
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

    # CWE-89: SQL Injection
    # Vulnerability: Using string concatenation to build SQL queries allows for SQL Injection.
    # Exploitable with user input in 'recipe_id'.
    # Impact: An attacker could execute arbitrary SQL commands or retrieve unauthorized data.
    # Example Payload: recipe_id = "1 OR 1=1"
    query = f"SELECT * FROM reviews WHERE recipe_id = {recipe_id}"
    cursor.execute(query)

    reviews = cursor.fetchall()
    conn.close()

    return jsonify(reviews), 200

if __name__ == '__main__':
    # CWE-489: Leftover Debug Code
    # Vulnerability: Running the application with debug=True in a production environment can expose sensitive information.
    # Impact: An attacker could gain insight into the application's internals through detailed error pages.
    app.run(debug=False)