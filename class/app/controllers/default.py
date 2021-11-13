from flask import render_template
from app import app


@app.route("/index")
@app.route("/")
def index():
    return render_template("app.html")

@app.route("/quemsomos")
def quem_somos():
    return render_template("quemsomos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")
