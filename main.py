from models import model_usuario
from models import model_produto

print("Criando tabelas no banco de dados...")

model_usuario.criar_tabela()
model_produto.criar_tabela()

print("Tabelas criadas com sucesso!")