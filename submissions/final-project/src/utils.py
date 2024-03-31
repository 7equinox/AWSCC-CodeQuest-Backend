# utils.py
from flask import redirect, url_for, request, session
from .model import PasswordEntry

# Function to redirect based on button id
def redirect_based_on_button_id(button_id):
    # Define a dictionary mapping button IDs to routes
    redirects = {
        1: 'add',
        2: 'view',
        3: 'search',
        4: 'delete',
        5: 'update'
    }
    # Redirect to the corresponding route based on the button ID
    return redirect(url_for(redirects[button_id]))

# Function to check if the database is empty
def check_database_empty():
    return not PasswordEntry.query.first()

# Function to handle search
def handle_search():
    search_term = get_search_term()
    entries = get_matching_entries(search_term)
    store_website_in_session(entries)
    return entries

# Function to get the search term from the form data
def get_search_term():
    return request.form['search'].strip().lower()

# Function to get entries that match the search term
def get_matching_entries(search_term):
    all_entries = PasswordEntry.query.all()
    return [entry for entry in all_entries if entry.website.strip().lower() == search_term]

# Function to store the website of the first entry in the session
def store_website_in_session(entries):
    if entries:
        session['website'] = entries[0].website