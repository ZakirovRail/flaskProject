import flask
# from report.views import report
# from blog.report.views import report

from blog.articles.views import articles_app
from blog.contacts.views import contact
from blog.user.views import user_app


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: flask.Flask):
    app.register_blueprint(user_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(contact)
