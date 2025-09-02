from flask import Blueprint, render_template

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    usuarios = ['Caio', 'Thiago', 'J.P.']
    return render_template('index.html', usuarios=usuarios)

@hello_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')
