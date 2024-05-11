from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Raiz():
    return render_template("index.html")

@app.route('/<string:nome>')
def error(nome):
    return f'<h1>A página ("{nome}" não existe)</h1>'

if __name__ == "__main__":
    app.run(debug=True)