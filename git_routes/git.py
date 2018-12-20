from flask import Blueprint, render_template, redirect

git = Blueprint('git', __name__, url_prefix='/gitlab')
@git.route("")
def index():
    return render_template('gitlab.html')
