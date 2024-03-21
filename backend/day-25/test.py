# import SQLite and Flask
from flask import Flask, render_template
import sqlite3

# Create a Flask App
app = Flask(__name__)
app.config["DB_NAME"] = "books.db"

# Connect to the Database
def get_db():
    db = sqlite3.connect(app.config["DB_NAME"])
    db.row_factory = sqlite3.Row
    return db

# Create a New Route
@app.route("/") 
def index():    
    conn = get_db()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template('index.html', books=books)


if __name__ == "__main__":
    app.run()