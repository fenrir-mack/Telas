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


@app.route("/criar-senha", methods=["GET", "POST"])
def criar_senha():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("criar_senha.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route("/projeto")
def projeto():
    # Página de um projeto específico
    return render_template("projeto.html")


@app.route("/empresa")
def empresa():
    return render_template("empresa.html")

@app.route("/empresa/membros")
def empresa_membros():
    return render_template("empresa_membros.html")

@app.route("/empresa/solicitacoes")
def empresa_solicitacoes():
    return render_template("empresa_solicitacoes.html")

@app.route("/empresa/configuracoes")
def empresa_configuracoes():
    return render_template("empresa_configuracoes.html")


@app.route("/projeto/membros")
def projeto_membros():
    return render_template("projeto_membros.html")

@app.route("/projeto/solicitacoes")
def projeto_solicitacoes():
    return render_template("projeto_solicitacoes.html")

@app.route("/projeto/configuracoes")
def projeto_configuracoes():
    return render_template("projeto_configuracoes.html")

@app.route("/empresas")
def empresas():
    return render_template("lista_empresas.html")

@app.route("/projetos")
def projetos():
    return render_template("lista_projetos.html")

if __name__ == "__main__":
    app.run(debug=True)