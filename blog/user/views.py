from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user_app = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')

USERS_DICT = {
    1: 'Alice',
    2: 'John',
    3: 'Mike'}


@user_app.route('/')
def user_list():
    return render_template('users/list.html', users=USERS_DICT)


@user_app.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS_DICT[pk]
    except KeyError:
        return NotFound()
    return render_template(
        'users/details.html',
        user_name=user_name
    )
