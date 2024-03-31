from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import path # to create the database file

DB_NAME = "new_books.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Connect to the database and create it if it doesn't exist
    from .model import Book # .model is the model.py file in the same directory
    if not path.exists("../instance/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")
        
    # Import and register the views blueprint
    from .views import views
    app.register_blueprint(views)
        
    return app
        
