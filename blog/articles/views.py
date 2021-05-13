from flask import Blueprint, render_template

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


@articles_app.route('/', endpoint='list')
def articles_list():
    # return render_template('articles/list.html', articles=[1, 2, 3, 4, 5])
    return render_template('articles/list.html', articles=ARTICLES)
