from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import model_usuario

templates = Jinja2Templates(directory="templates")

model_usuario.criar_tabela()

def mostrar_usuarios(request: Request):
    usuarios = model_usuario.listar_usuarios() #Cria essa função "listar_usuarios" na model
    return templates.TemplateResponse("usuarios/index.html", {"request": request, "usuarios": usuarios})

def mostrar_edicao_usuario(request: Request, idUsuario: int):
    usuario = model_usuario.buscar_usuario_por_id(idUsuario) #Cria essa função "buscar_usuario_por_id" na model
    usuarios = model_usuario.listar_usuario()
    return templates.TemplateResponse("usuarios/editar.html", {"request": request, "usuario": usuario, "usuarios": usuarios})

async def cadastrar_usuario(request: Request, nome: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    model_usuario.inserir_usuario(nome, email, senha) #Cria essa função "inserir_usuario" na model
    return RedirectResponse("/usuarios", status_code=303)

def excluir_usuario(idUsuario: int):
    model_usuario.excluir_usuario(idUsuario) #Cria essa função "excluir_usuario" na model
    return RedirectResponse("/usuarios", status_code=303)

async def atualizar_usuario(request: Request, idUsuario: int, nome: str = Form(...), email: str = Form(...), senha: str = Form(...)):
    model_usuario.atualizar_usuario(idUsuario, nome, email, senha) #Cria essa função "atualizar_usuario" na model
    return RedirectResponse("/usuarios", status_code=303)
    
#usa os mesmos nomes pras variáveis no banco de dados 'idUsuario', 'nome', 'email', 'senha'; lembra de usar os mesmos formatos também int, string, string, etc