from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, PasswordEntry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website = request.form['website']
        email = request.form['email']
        password = request.form['password']
        new_entry = PasswordEntry(website=website, email=email, password=password)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('index'))
    passwords = PasswordEntry.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    entry = PasswordEntry.query.get_or_404(id)
    entry.website = request.form['website']
    entry.email = request.form['email']
    entry.password = request.form['password']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    entry = PasswordEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)