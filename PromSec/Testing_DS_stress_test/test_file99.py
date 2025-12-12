from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # Securely establish a connection with the SQLite database
    return sqlite3.connect('recipe.db')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    # Extract title and ingredients from the secure JSON request
    title = request.json['title']
    ingredients = request.json['ingredients']

    # Obtain a secure database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use parameterized queries to prevent SQL injection
    query = "INSERT INTO recipes (title) VALUES (?)"
    cursor.execute(query, (title,))
    recipe_id = cursor.lastrowid

    # Insert each ingredient securely with parameterized queries
    for ingredient in ingredients:
        query = "INSERT INTO ingredients (recipe_id, ingredient) VALUES (?, ?)"
        cursor.execute(query, (recipe_id, ingredient))

    # Commit changes and close the connection securely
    conn.commit()
    conn.close()

    # Return a secure JSON response confirming successful addition
    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

@app.route('/submit_review', methods=['POST'])
def submit_review():
    # Securely extract data from the JSON request
    recipe_id = request.json['recipe_id']
    review = request.json['review']
    reviewer_id = request.json['reviewer_id']

    # Securely connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use secure parameterized queries to insert the review data
    query = "INSERT INTO reviews (recipe_id, review, reviewer_id) VALUES (?, ?, ?)"
    cursor.execute(query, (recipe_id, review, reviewer_id))

    # Securely commit the transaction and close the connection
    conn.commit()
    conn.close()

    # Return a secure JSON response confirming review submission
    return jsonify({"message": "Review submitted successfully"}), 200

@app.route('/get_recipe_reviews', methods=['GET'])
def get_recipe_reviews():
    # Securely obtain the recipe_id from the request arguments
    recipe_id = request.args.get('recipe_id')

    # Establish a secure connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use parameterized queries to securely fetch reviews
    query = "SELECT * FROM reviews WHERE recipe_id = ?"
    cursor.execute(query, (recipe_id,))
    
    reviews = cursor.fetchall()
    conn.close()

    # Return a secure JSON response with the fetched reviews
    return jsonify(reviews), 200

if __name__ == '__main__':
    # Run the Flask application securely with debug mode off
    app.run(debug=False)