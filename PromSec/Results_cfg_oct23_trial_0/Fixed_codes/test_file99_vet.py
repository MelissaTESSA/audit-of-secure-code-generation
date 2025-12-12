import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = 'recipe.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER,
                    ingredient TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER,
                    review TEXT,
                    reviewer_id INTEGER
                )''')
    conn.commit()
    conn.close()

create_tables()

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    data = request.get_json()
    title = data.get('title')
    ingredients = data.get('ingredients')

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('INSERT INTO recipes (title) VALUES (?)', (title,))
    recipe_id = c.lastrowid

    for ingredient in ingredients:
        c.execute('INSERT INTO ingredients (recipe_id, ingredient) VALUES (?, ?)', (recipe_id, ingredient))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Recipe added successfully', 'recipe_id': recipe_id})

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.get_json()
    recipe_id = data.get('recipe_id')
    review = data.get('review')
    reviewer_id = data.get('reviewer_id')

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('INSERT INTO reviews (recipe_id, review, reviewer_id) VALUES (?, ?, ?)', (recipe_id, review, reviewer_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Review submitted successfully'})

@app.route('/get_recipe_reviews', methods=['GET'])
def get_recipe_reviews():
    recipe_id = request.args.get('recipe_id')

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('SELECT review, reviewer_id FROM reviews WHERE recipe_id = ?', (recipe_id,))
    reviews = c.fetchall()

    conn.close()

    return jsonify(reviews)

if __name__ == '__main__':
    app.run()