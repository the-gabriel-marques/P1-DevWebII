from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, constr
from models import model_usuario

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class UsuarioBase(BaseModel):
    nome: constr(min_length=3)
    email: EmailStr
    senha: constr(min_length=6)

@router.get("/cadastro_usuario", response_class=HTMLResponse)
def formulario_usuario(request: Request):
    return templates.TemplateResponse("usuario.html", {"request": request})

@router.post("/usuarios")
async def cadastrar_usuario(request: Request):
    try:
        form = await request.json()
        nome = form.get("nome")
        email = form.get("email")
        senha = form.get("senha")

        if not nome or len(nome) < 3:
            return JSONResponse(status_code=400, content={"mensagem": "Nome inválido"})
        if not email or "@" not in email:
            return JSONResponse(status_code=400, content={"mensagem": "Email inválido"})
        if not senha or len(senha) < 6:
            return JSONResponse(status_code=400, content={"mensagem": "Senha muito curta"})

        model_usuario.inserir_usuario(nome, email, senha)
        return {"mensagem": "Usuário cadastrado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.get("/usuarios", response_class=JSONResponse)
def listar_usuarios():
    try:
        return model_usuario.listar_usuarios()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {str(e)}")

@router.get("/usuarios/{idUsuario}", response_class=JSONResponse)
def buscar_usuario(idUsuario: int):
    try:
        usuario = model_usuario.buscar_usuario_por_id(idUsuario)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@router.put("/usuarios/{idUsuario}", response_class=JSONResponse)
async def atualizar_usuario(idUsuario: int, usuario: UsuarioBase):
    try:
        existente = model_usuario.buscar_usuario_por_id(idUsuario)
        if not existente:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        model_usuario.atualizar_usuario(idUsuario, usuario.nome, usuario.email, usuario.senha)
        return {"mensagem": "Usuário atualizado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar usuário: {str(e)}")

@router.delete("/usuarios/{idUsuario}", response_class=JSONResponse)
def excluir_usuario(idUsuario: int):
    try:
        existente = model_usuario.buscar_usuario_por_id(idUsuario)
        if not existente:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        model_usuario.excluir_usuario(idUsuario)
        return {"mensagem": "Usuário excluído com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir usuário: {str(e)}")