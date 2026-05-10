from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("cadastro.html")


@app.route("/esqueceu-senha", methods=["GET", "POST"])
def esqueceu_senha():
    if request.method == "POST":
        return redirect(url_for("confirmacao_senha"))
    return render_template("esqueceu_senha.html")


@app.route("/confirmacao-senha")
def confirmacao_senha():
    return render_template("confirmacao_senha.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes.html")

@app.route("/empresas")
def empresas():
    return render_template("empresas.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

if __name__ == "__main__":
    app.run(debug=True)