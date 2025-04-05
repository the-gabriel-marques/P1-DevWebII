from fastapi import FastAPI
from controller.controller_produto import router as produto_router
from controller.controller_usuario import router as usuario_router

app = FastAPI()

app.include_router(usuario_router)
app.include_router(produto_router)

from models import model_usuario
from models import model_produto

print("Criando tabelas no banco de dados...")

model_usuario.criar_tabela()
model_produto.criar_tabela()

print("Tabelas criadas com sucesso!")