from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import model_produtos

templates = Jinja2Templates(directory="templates")

model_produtos.criar_tabela()

def mostrar_produtos(request: Request):
    produtos = model_produtos.listar_produtos() #Cria essa função "listar_produtos" na model
    return templates.TemplateResponse("produtos/index.html", {"request": request, "produtos": produtos})

def mostrar_edicao_produto(request: Request, idProduto: int):
    produto = model_produtos.buscar_produto_por_id(idProduto) #Cria essa função "buscar_produto_por_id" na model
    produtos = model_produtos.listar_produtos()
    return templates.TemplateResponse("produtos/editar.html", {"request": request, "produto": produto, "produtos": produtos})

async def cadastrar_produto(request: Request, nome: str = Form(...), preco: float = Form(...), estoque: int = Form(...)):
    model_produtos.inserir_produto(nome, preco, estoque) #Cria essa função "inserir_produto" na model
    return RedirectResponse("/produtos", status_code=303)

def excluir_produto(idProduto: int):
    model_produtos.excluir_produto(idProduto) #Cria essa função "excluir_produto" na model
    return RedirectResponse("/produtos", status_code=303)

async def atualizar_produto(request: Request, idProduto: int, nome: str = Form(...), preco: float = Form(...), estoque: int = Form(...)):
    model_produtos.atualizar_produto(idProduto, nome, preco, estoque) #Cria essa função "atualizar_produto" na model
    return RedirectResponse("/produtos", status_code=303)

#usa os mesmos nomes pras variáveis no banco de dados 'idProduto', 'nome', 'preco', 'estoque'; lembra de usar os mesmos formatos também int, string, float, etc
