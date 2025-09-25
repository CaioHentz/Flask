from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import User, db
from .forms import UserForm

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')
def index():
    usuarios = User.query.all()
    form = UserForm()
    return render_template('index.html', usuarios=usuarios, form=form)

@hello_bp.route('/novoUsuario', methods = ['POST'])
def novoUsuario():
    form = UserForm()
    if form.validate_on_submit():

        username = form.username.data
        novo_usuario = User(username = username)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Usuario criado com sucesso!', 'success')

    else:

        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error on field'{getattr(form,field).label.text}': {error}", 'danger')

    return redirect(url_for('hello.index'))


@hello_bp.route('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuario removido com sucesso!", 'success')
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    form = UserForm(obj=usuario)
    if form.validate_on_submit():
        usuario.username = form.username.data
        db.session.commit()
        flash('Usuario atualizado com sucesso!', 'success')

    else:

        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error on field'{getattr(form,field).label.text}': {error}", 'danger')
    return redirect(url_for('hello.index'))
