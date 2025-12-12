from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    # This will connect to the 'recipe.db' file
    return sqlite3.connect('recipe.db')

# Route to add a new recipe
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    # Get the recipe title and ingredients from the request
    title = request.json['title']
    ingredients = request.json['ingredients']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert the recipe title into the recipes table
    query = f"INSERT INTO recipes (title) VALUES ('{title}')"
    cursor.execute(query)
    # Get the id of the newly inserted recipe
    recipe_id = cursor.lastrowid

    # Loop through each ingredient and insert it into the ingredients table
    for ingredient in ingredients:
        query = f"INSERT INTO ingredients (recipe_id, ingredient) VALUES ({recipe_id}, '{ingredient}')"
        cursor.execute(query)

    # Save the changes and close the connection
    conn.commit()
    conn.close()

    # Return a success message with the new recipe ID
    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

# Route to submit a review for a recipe
@app.route('/submit_review', methods=['POST'])
def submit_review():
    # Get the recipe ID, review text, and reviewer ID from the request
    recipe_id = request.json['recipe_id']
    review = request.json['review']
    reviewer_id = request.json['reviewer_id']

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert the new review into the reviews table
    query = f"INSERT INTO reviews (recipe_id, review, reviewer_id) VALUES ({recipe_id}, '{review}', '{reviewer_id}')"
    cursor.execute(query)

    # Save the changes and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({"message": "Review submitted successfully"}), 200

# Route to get all reviews for a specific recipe
@app.route('/get_recipe_reviews', methods=['GET'])
def get_recipe_reviews():
    # Get the recipe ID from the request arguments
    recipe_id = request.args.get('recipe_id')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Select all reviews for the given recipe ID
    query = f"""
    SELECT r.review, COUNT(r.id) as review_count
    FROM reviews r
    WHERE r.recipe_id = {recipe_id}
    GROUP BY r.id
    """
    cursor.execute(query)
    
    # Fetch all the results
    reviews = cursor.fetchall()
    conn.close()

    # Return the reviews in JSON format
    return jsonify(reviews), 200

# Start the Flask application
if __name__ == '__main__':
    # Run the app with debug mode off
    app.run(debug=False)