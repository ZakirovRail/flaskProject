from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

contact = Blueprint('contact', __name__, url_prefix='/contacts', static_folder='../static')


@contact.route('/contacts')
def contacts_page():
    return render_template('contacts/contacts.html')
