from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint('articles_app', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = [
    {
        'id': 1,
        'title': 'First Alice article',
        'text': 'This is article of Alice',
        'author': {
            'name': 'some name',
            'id': 1,
        },
    },
    {
        'id': 2,
        'title': 'First John article',
        'text': 'This is article of Alice',
        'author': {
            'name': 'some name',
            'id': 2,
        },
    },
    {
        'id': 3,
        'title': 'First Mike article',
        'text': 'This is article of Mike',
        'author': {
            'name': 'some name',
            'id': 3,
        },
    }
]


@articles_app.route('/')
# @articles_app.route('/<int:id_art>')
# def articles_list(id_art: int):
def articles_list():
    try:
        id_art = [id['id'] for id in ARTICLES]
    except KeyError:
        return NotFound()
    return render_template('articles/list.html', articles=id_art)


# @user.route('/<int:pk>')
# def get_user(pk: int):
#     try:
#         user_name = USERS[pk]
#     except KeyError:
#         return NotFound()
#     return render_template(
#         'users/details.html',
#         user_name=user_name
#     )
