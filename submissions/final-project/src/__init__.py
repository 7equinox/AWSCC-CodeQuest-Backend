# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

# Instantiate a new Flask web server
app = Flask(__name__, template_folder='templates')
# Set up the SQLAlchemy object to connect to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
# Turn off the SQLAlchemy event system as it's not required
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Generate a secret key for session signing and CSRF protection
app.config['SECRET_KEY'] = secrets.token_hex(64)

# Instantiate a SQLAlchemy object for our ORM
db = SQLAlchemy(app)

# Import the models module so SQLAlchemy is aware of the PasswordEntry model
from src import model

# Create the database tables
with app.app_context():
    db.create_all()

# Import the views module to register the routes with the Flask application
from src import views
