from flask import Blueprint, render_template

report = Blueprint('reports', __name__, url_prefix='/reports', static_folder='../static')


@report.route('/')
def report_list():
    return render_template('reports/list.html', reports=[1, 2, 3, 4, 5])
