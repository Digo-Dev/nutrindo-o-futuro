from flask import render_template, Blueprint, request, redirect, flash
from database.conectionDB import conectar, conexao

login_route = Blueprint('login', __name__)

@login_route.route('/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@login_route.route('/autenticar', methods=['POST'])
def autenticar():
    login = request.form.get('usuario')
    senha = request.form.get('senha')

    global logado
    conectar()
    cont = 0
    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute('select * from users;')
        usuariosBD = cursor.fetchall()
        
        for usuario in usuariosBD:
            cont += 1
            usuarioNome = str(usuario[2])
            usuarioSenha = str(usuario[3])

            if usuarioNome == login and usuarioSenha == senha:
                logado = True
                return redirect('/home')

            if cont >= len(usuariosBD):
                flash('USUARIO INVALIDO')
                return redirect('/')
    else:
        return redirect('/')