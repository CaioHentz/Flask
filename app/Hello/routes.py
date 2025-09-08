from flask import Blueprint, render_template
from ..models import User, db

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)

@hello_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')
