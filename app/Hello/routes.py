from flask import Blueprint, render_template

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    return render_template('index.html')

@hello_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')
