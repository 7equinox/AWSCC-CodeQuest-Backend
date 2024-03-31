from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)