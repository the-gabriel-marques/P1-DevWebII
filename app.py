from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 


produtos = []
usuarios = []
produto_id_counter = 1


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/<int:id>", methods=["GET"])
def obter_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route("/produtos", methods=["POST"])
def criar_produto():
    global produto_id_counter
    dados = request.json
    if not all(k in dados for k in ("nome", "preco", "estoque")):
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400

    novo = {
        "id": produto_id_counter,
        "nome": dados["nome"],
        "preco": float(dados["preco"]),
        "estoque": int(dados["estoque"])
    }
    produtos.append(novo)
    produto_id_counter += 1
    return jsonify(novo), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.json
    for produto in produtos:
        if produto["id"] == id:
            produto["nome"] = dados.get("nome", produto["nome"])
            produto["preco"] = float(dados.get("preco", produto["preco"]))
            produto["estoque"] = int(dados.get("estoque", produto["estoque"]))
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({"mensagem": "Produto removido com sucesso"})
    return jsonify({"erro": "Produto não encontrado"}), 404


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json
    if not all(k in dados for k in ("nome", "email", "senha")):
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400

    novo = {
        "id": len(usuarios) + 1,
        "nome": dados["nome"],
        "email": dados["email"],
        "senha": dados["senha"]  
    }
    usuarios.append(novo)
    return jsonify(novo), 201



if __name__ == "__main__":
    app.run(debug=True)
