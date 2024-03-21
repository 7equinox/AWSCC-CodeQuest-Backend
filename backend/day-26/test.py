# Create Flask App and connect to SQLite Database
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_books.db'
db = SQLAlchemy(app)


# Define a Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}-{self.author}>'
    
    
# Create the Database and Interact with the Database
with app.app_context():
    db.create_all() # create the database
    new_book = Book(title="To Kill a Mockingbird", author="Harper Lee", published_year=1960)
    # take note that the new_book is an instance of the Book class
    # and we are adding it to the database using the db.session.add() method
    # so if there is same book title and author, it will not be added to the database
    # and it will raise an error
    db.session.add(new_book)
    db.session.commit()


# Create a New Route
@app.route("/") 
def index():    
    books = Book.query.all()
    return render_template('index.html', books=books)


if __name__ == "__main__":
    app.run()