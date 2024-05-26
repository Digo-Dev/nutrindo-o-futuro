from flask import render_template, Blueprint, redirect

# Declaração da blueprint "logout"
logout_route = Blueprint('logout', __name__)

# Rotas da blueprint "logout"
@logout_route.route('/logout')
def logout():
    global logado
    logado = False
    return redirect('/')