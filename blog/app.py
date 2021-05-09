import flask
# from report.views import report
from blog.report.views import report
from blog.user.views import user


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: flask.Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
