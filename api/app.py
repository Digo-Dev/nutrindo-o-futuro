from flask import Flask
from routes.login import login_route
from routes.home import home_route
from routes.produto import produto_route
from routes.logout import logout_route
from databases.conectionDB import conectar

app = Flask(__name__)
app.config['SECRET_KEY'] ='nopass'

# Registro das blueprints
app.register_blueprint(login_route)
app.register_blueprint(home_route, url_prefix='/home')
app.register_blueprint(produto_route, url_prefix='/produto')
app.register_blueprint(logout_route)

# Quando iniciada a aplicação o usuário tem o  status de deslogado atribuido 
# e é conectado ao banco de dados


conectar()

if __name__ == "__main__":
    app.run(debug=True)