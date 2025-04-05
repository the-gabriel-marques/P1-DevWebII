from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, constr, condecimal, conint
from models import model_produto
from starlette.status import HTTP_302_FOUND

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro", response_class=HTMLResponse)
def formulario_produto(request: Request, mensagem: str = ""):
    return templates.TemplateResponse("index.html", {"request": request, "mensagem": mensagem})

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
async def cadastrar_produto(request: Request):
    form = await request.json()
    nome = form.get("nome")
    preco = form.get("preco")
    estoque = form.get("estoque")

    if not nome or len(nome) < 3:
        return RedirectResponse(url="/cadastro?mensagem=Nome inválido", status_code=HTTP_302_FOUND)
    if not preco or float(preco) <= 0:
        return RedirectResponse(url="/cadastro?mensagem=Preço inválido", status_code=HTTP_302_FOUND)
    if estoque is None or int(estoque) < 0:
        return RedirectResponse(url="/cadastro?mensagem=Estoque inválido", status_code=HTTP_302_FOUND)

    model_produto.inserir_produto(nome, float(preco), int(estoque))
    return RedirectResponse(url="/cadastro?mensagem=Produto cadastrado com sucesso!", status_code=HTTP_302_FOUND)

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