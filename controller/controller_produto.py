from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr, condecimal, conint
from models import model_produto

router = APIRouter()

class ProdutoAtualizar(BaseModel):
    nome: constr(min_length=3)
    preco: condecimal(gt=0)
    estoque: conint(ge=0)

class ProdutoCriar(BaseModel):
    nome: constr(min_length=3)
    preco: condecimal(gt=0)
    estoque: conint(ge=0)

@router.get("/produtos")
def listar_produtos():
    produtos = model_produto.listar_produtos()
    return produtos

@router.get("/produtos/{idProduto}")
def buscar_produto(idProduto: int):
    produto = model_produto.buscar_produto_por_id(idProduto)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.post("/produtos")
def cadastrar_produto(produto: ProdutoCriar):
    model_produto.inserir_produto(produto.nome, float(produto.preco), produto.estoque)
    return {"mensagem": "Produto cadastrado com sucesso"}

@router.put("/produtos/{idProduto}")
def atualizar_produto(idProduto: int, dados: ProdutoAtualizar):
    produto_existente = model_produto.buscar_produto_por_id(idProduto)
    if not produto_existente:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    model_produto.atualizar_produto(idProduto, dados.nome, float(dados.preco), dados.estoque)
    return {"mensagem": "Produto atualizado com sucesso"}

@router.delete("/produtos/{idProduto}")
def excluir_produto(idProduto: int):
    produto_existente = model_produto.buscar_produto_por_id(idProduto)
    if not produto_existente:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    model_produto.excluir_produto(idProduto)
    return {"mensagem": "Produto excluído com sucesso"}