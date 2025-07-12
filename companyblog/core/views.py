from flask import render_template, redirect, Blueprint

core = Blueprint('core', __name__)  # no leading slash in blueprint name!

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('info.html')
