from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import mysql.connector
import bcrypt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Função de conexão ao banco (pode estar em db.py)
def conectar():
    return mysql.connector.connect(host='localhost', user='root', password=' ', database='mydb')

# Models
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

# Endpoints de produtos
@app.get("/produtos", response_model=List[ProdutoOut])
def listar_produtos():
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    db.close()
    return produtos

@app.get("/produtos/{id}", response_model=ProdutoOut)
def obter_produto(id: int):
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos WHERE idProduto = %s", (id,))
    produto = cursor.fetchone()
    db.close()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos", response_model=ProdutoOut, status_code=201)
def criar_produto(produto: Produto):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)", 
                   (produto.nome, produto.preco, produto.estoque))
    db.commit()
    id_novo = cursor.lastrowid
    db.close()
    return { "id": id_novo, **produto.dict() }

@app.put("/produtos/{id}", response_model=ProdutoOut)
def atualizar_produto(id: int, produto: Produto):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE idProduto=%s", 
                   (produto.nome, produto.preco, produto.estoque, id))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.commit()
    db.close()
    return { "id": id, **produto.dict() }

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE idProduto=%s", (id,))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.commit()
    db.close()
    return {"mensagem": "Produto removido com sucesso"}

# Endpoints de usuários
@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    db = conectar()
    cursor = db.cursor()

    # Hash de senha
    hashed_senha = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", 
                       (usuario.nome, usuario.email, hashed_senha))
        db.commit()
        id_novo = cursor.lastrowid
        db.close()
        return {"id": id_novo, "nome": usuario.nome, "email": usuario.email}
    except mysql.connector.Error as err:
        db.close()
        raise HTTPException(status_code=400, detail="Erro ao criar usuário: " + str(err))
