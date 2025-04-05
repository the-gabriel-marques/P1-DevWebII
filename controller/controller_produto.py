from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from models import model_produto
from pydantic import BaseModel, constr, condecimal, conint

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class ProdutoAtualizar(BaseModel):
    nome: constr(min_length=3)
    preco: condecimal(gt=0)
    estoque: conint(ge=0)

@router.get("/cadastro", response_class=HTMLResponse)
def formulario_produto(request: Request, mensagem: str = ""):
    try:
        return templates.TemplateResponse("index.html", {"request": request, "mensagem": mensagem})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.get("/produtos", response_class=JSONResponse)
def listar_produtos():
    try:
        return model_produto.listar_produtos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.get("/produtos/{idProduto}", response_class=JSONResponse)
def buscar_produto(idProduto: int):
    try:
        produto = model_produto.buscar_produto_por_id(idProduto)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return produto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.post("/produtos")
async def cadastrar_produto(request: Request):
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.put("/produtos/{idProduto}", response_class=JSONResponse)
def atualizar_produto(idProduto: int, dados: ProdutoAtualizar):
    try:
        existente = model_produto.buscar_produto_por_id(idProduto)
        if not existente:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        model_produto.atualizar_produto(idProduto, dados.nome, float(dados.preco), dados.estoque)
        return {"mensagem": "Produto atualizado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.delete("/produtos/{idProduto}", response_class=JSONResponse)
def excluir_produto(idProduto: int):
    try:
        existente = model_produto.buscar_produto_por_id(idProduto)
        if not existente:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        model_produto.excluir_produto(idProduto)
        return {"mensagem": "Produto excluído com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")