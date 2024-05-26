from flask import render_template, Blueprint, request, redirect, flash
from databases.conectionDB import conectar, conexao


# Declaração da blueprint "Login"
login_route = Blueprint('login', __name__)

# Rotas da blueprint "login" - Rota principal
@login_route.route('/', methods=['GET','POST'])
def login():
    return render_template('login.html')

# Rota responsavel por chamar o metodo que recupera o 
# login e senha digitados na pagina de login e buscar no
# banco de dados o osuário e senha
@login_route.route('/autenticar', methods=['POST'])
def autenticar():
    login = request.form.get('usuario')
    senha = request.form.get('senha')

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
                flash('Usuário ou senha inválidos!')
                return redirect('/')
    else:
        return redirect('/')