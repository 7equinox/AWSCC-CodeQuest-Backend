# model.py
from . import db

# Create a new model for the database to store password entries
class PasswordEntry(db.Model):
    # Define an id for each entry, which serves as the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Define the website, email, and password fields, which cannot be null
    website = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
