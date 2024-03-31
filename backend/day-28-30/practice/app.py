from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    passwords = PasswordEntry.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/add', methods=['POST'])
def add_password():
    website = request.form.get('website')
    email = request.form.get('email')
    password = request.form.get('password')
    new_entry = PasswordEntry(website=website, email=email, password=password)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_password(id):
    entry = PasswordEntry.query.get_or_404(id)
    entry.website = request.form.get('website')
    entry.email = request.form.get('email')
    entry.password = request.form.get('password')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_password(id):
    entry = PasswordEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)