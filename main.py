from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from controller.controller_produto import router as produto_router
from controller.controller_usuario import router as usuario_router

from models import model_usuario
from models import model_produto

# Inicializa o app FastAPI
app = FastAPI()

# Inclui os routers
app.include_router(usuario_router)
app.include_router(produto_router)

# Configura templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")

# Rota da página inicial
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.on_event("startup")
def startup_event():
    print("Inicializando tabelas no banco de dados...")
    model_usuario.criar_tabela()
    model_produto.criar_tabela()
    print("Tabelas criadas com sucesso!")
