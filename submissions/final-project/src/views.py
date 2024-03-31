# views.py
# Import necessary modules and objects
from functools import wraps
from flask import render_template, request, redirect, url_for, session
from . import app, db
from .model import PasswordEntry
from .utils import check_database_empty, redirect_based_on_button_id, handle_search

# Decorator to check if the database is empty
def check_db_empty(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if check_database_empty():
            session['message'] = 'No inputs found!'
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Define the route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Get the message from the session, defaulting to 'Welcome!'
    message = session.pop('message', 'Welcome!')
    # If the request method is POST, redirect based on the button ID
    if request.method == 'POST':
        button_id = int(request.form.get('button'))
        return redirect_based_on_button_id(button_id)
    # Otherwise, render the index page with the message
    return render_template('index.html', message=message)

# Define the route for the add page
@app.route('/add', methods=['GET', 'POST'])
def add():
    # If the request method is POST, process the form data
    if request.method == 'POST':
        button_id = request.form.get('button')
        # If the back button was clicked, redirect to the index page
        if button_id == 'back':
            return redirect(url_for('index'))
        # Otherwise, get the form data and add a new password entry
        website = request.form['website'].strip()
        email = request.form['email'].strip()
        password = request.form['password']
        # Check if an entry with the same website and email already exists
        existing_entry = PasswordEntry.query.filter_by(website=website, email=email).first()
        if existing_entry:
            # If it does, set a message in the session
            session['message'] = 'Account existed!'
        else:
            # Otherwise, create a new entry and add it to the database
            new_entry = PasswordEntry(website=website, email=email, password=password)
            db.session.add(new_entry)
            db.session.commit()
            # Set a success message in the session
            session['message'] = 'Added successfully!'
        # Redirect to the index page
        return redirect(url_for('index'))
    # If the request method is GET, render the add page
    return render_template('add.html')

# Define the route for the view page
@app.route('/view', methods=['GET', 'POST'])
@check_db_empty
def view():
    # Get all password entries from the database
    entries = PasswordEntry.query.all()
    # If the request method is POST, redirect to the index page
    if request.method == 'POST':
        return redirect(url_for('index'))
    # Otherwise, render the view page with the entries
    return render_template('view.html', entries=entries)

# Define the route for the search page
@app.route('/search', methods=['GET', 'POST'])
@check_db_empty
def search():
    # Initialize a flag to indicate whether the search button was clicked
    search_clicked = False
    # If the request method is POST, process the form data
    if request.method == 'POST':
        button_id = request.form.get('button')
        # If the back button was clicked, redirect to the index page
        if button_id == 'back':
            return redirect(url_for('index'))
        else:
            # Otherwise, handle the search and set the flag to True
            entries = handle_search()
            search_clicked = True
            # Render the search page with the search results
            return render_template('search.html', search_term=session.get('website', ''), entries=entries, search_clicked=search_clicked)
    # If the request method is GET, render the search page
    return render_template('search.html')

# Define the route for the delete page
@app.route('/delete', methods=['GET', 'POST'])
@check_db_empty
def delete():
    # Initialize a flag to indicate whether the search button was clicked
    search_clicked = False
    # If the request method is POST, process the form data
    if request.method == 'POST':
        button_id = request.form.get('button')
        # If the back button was clicked, redirect to the index page
        if button_id == 'back':
            return redirect(url_for('index'))
        elif button_id == 'Search':
            # If the search button was clicked, handle the search and set the flag to True
            entries = handle_search()
            search_clicked = True
            # Render the delete page with the search results
            return render_template('delete.html', search_term=session.get('website', ''), entries=entries, search_clicked=search_clicked)
        else:
            # If another button was clicked, delete the corresponding entry
            entry_id = int(button_id)
            entry = PasswordEntry.query.get(entry_id)
            if entry:
                # If the entry exists, delete it from the database
                db.session.delete(entry)
                db.session.commit()
                # Set a success message in the session
                session['message'] = 'Deleted successfully!'
                # Redirect to the index page
                return redirect(url_for('index'))
    # If the request method is GET, render the delete page
    return render_template('delete.html')

# Define the route for the update page
@app.route('/update', methods=['GET', 'POST'])
@check_db_empty
def update():
    # Initialize flags to indicate whether the search or update button was clicked
    search_clicked = False
    update_clicked = False
    # Initialize an empty list for the entries and a None value for the entry
    entries = []
    entry = None
    # If the request method is POST, process the form data
    if request.method == 'POST':
        button_id = request.form.get('button')
        # If the back button was clicked, redirect to the index page
        if button_id == 'back':
            return redirect(url_for('index'))
        elif button_id == 'Search':
            # If the search button was clicked, handle the search and set the flag to True
            entries = handle_search()
            session['entries'] = [entry.id for entry in entries]
            search_clicked = True
        elif button_id == 'back_to_list':
            # If the back to list button was clicked, get the entries from the session and set the flag to True
            entries = PasswordEntry.query.filter(PasswordEntry.id.in_(session.get('entries', []))).all()
            search_clicked = True
        else:
            # If another button was clicked, get the corresponding entry
            entry_id = int(button_id)
            entry = PasswordEntry.query.get(entry_id)
            if entry:
                # If the entry exists and the form data includes website, email, and password, update the entry
                if 'website' in request.form and 'email' in request.form and 'password' in request.form:
                    entry.website = request.form['website'].strip()
                    entry.email = request.form['email'].strip()
                    entry.password = request.form['password']
                    db.session.commit()
                    # Set a success message in the session
                    session['message'] = 'Updated successfully!'
                    # Redirect to the index page
                    return redirect(url_for('index'))
                else:
                    # Otherwise, set the update flag to True
                    update_clicked = True
    # Render the update page with the search results and the entry to update
    return render_template('update.html', search_term=session.get('website', ''), entries=entries, search_clicked=search_clicked, update_clicked=update_clicked, entry=entry)
