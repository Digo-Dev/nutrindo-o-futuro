from flask import Flask, render_template
from routes.login import login_route
from routes.home import home_route
from routes.produto import produto_route
from database.conectionDB import conectar

app = Flask(__name__)
app.config['SECRET_KEY'] ='nopass'

app.register_blueprint(login_route)
app.register_blueprint(home_route, url_prefix='/home')
app.register_blueprint(produto_route, url_prefix='/produto')

logado = False
conectar()

if __name__ == "__main__":
    app.run(debug=True)