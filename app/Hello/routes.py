from flask import Blueprint, render_template, request, redirect, url_for
from ..models import User, db

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)

@hello_bp.route('/novoUsuario', methods = ['POST'])
def novoUsuario():
    username = request.form['nome-usuario']

    novo_usuario = User(username = username)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect('/')

@hello_bp.route('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        usuario.username = request.form['nome_usuario']
        db.session.commit()
    return redirect(url_for('hello.index'))
