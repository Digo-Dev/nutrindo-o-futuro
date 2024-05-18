from flask import Flask, render_template
from routes.home import home_route
from routes.produto import produto_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(produto_route, url_prefix='/produto')

"""
@app.route('/')
def Raiz():
    return render_template('index.html')

@app.route('/cadastro.html')
def cadastra():
    return render_template('cadastro.html')

@app.route('/entradas.html')
def entradas():
    return render_template('entradas.html')

@app.route('/saidas.html')
def saidas():
    return render_template('saidas.html')

@app.route('/estoque.html')
def estoque():
    return render_template('estoque.html')


@app.route('/<string:nome>')
def error(nome):
    return f'<h1>A página ("{nome}" não existe)</h1>'
"""

if __name__ == "__main__":
    app.run(debug=True)