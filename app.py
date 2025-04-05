from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


produtos = []
usuarios = []
produto_id_counter = 1



class Produto(BaseModel):
    nome: str
    preco: float
    estoque: int

class ProdutoOut(Produto):
    id: int

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str


# Endpoints de produtos (Confirmar se funciona)
@app.get("/produtos", response_model=List[ProdutoOut])
def listar_produtos():
    return produtos

@app.get("/produtos/{id}", response_model=ProdutoOut)
def obter_produto(id: int):
    for produto in produtos:
        if produto["id"] == id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.post("/produtos", response_model=ProdutoOut, status_code=201)
def criar_produto(produto: Produto):
    global produto_id_counter
    novo = {
        "id": produto_id_counter,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque
    }
    produtos.append(novo)
    produto_id_counter += 1
    return novo

@app.put("/produtos/{id}", response_model=ProdutoOut)
def atualizar_produto(id: int, produto: Produto):
    for p in produtos:
        if p["id"] == id:
            p["nome"] = produto.nome
            p["preco"] = produto.preco
            p["estoque"] = produto.estoque
            return p
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return {"mensagem": "Produto removido com sucesso"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")


# Endpoints de usuários (Confirmar se está certo, tenho dúvidas)
@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    novo = {
        "id": len(usuarios) + 1,
        "nome": usuario.nome,
        "email": usuario.email,
        "senha": usuario.senha  
    }
    usuarios.append(novo)
    return novo



