from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {
        "id": 1,
        "nome": "Krysthian"
    },
    {
        "id": 2,
        "nome": "João"
    }
]

@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "API Connect funcionando",
        "status": "online"
    })

@app.route("/usuarios")
def listar_usuarios():
    return jsonify(usuarios)
@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()

    if not dados or not dados.get("nome") or not dados.get("email"):
        return jsonify({
            "error": "Os campos nome e e-mail são obrigatórios."
        }), 400

    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201
@app.route("/usuarios/<int:id>")
def buscar_usuario(id):

    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify(usuario)

    return jsonify({
        "erro": "Usuário não encontrado"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)