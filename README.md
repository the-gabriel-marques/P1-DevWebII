# ⚙️ Sistema de Gerenciamento de Produtos e Usuários
Projeto de avaliação para a P1 de Desenvolvimento Web II

## 🔴 Funcionalidades
- Cadastro de Usuários com Validação
- Cadastro de Produtos
- Atualização de Usuários e Produtos
- Interface Gráfica para Cadastro de Usuários e Produtos
- Conexão com Banco de Dados usando O MySQL
- Inicialização Automática das tabelas ao rodar o Servidor

## 🟠 Tecnologias Utilizadas
- FastAPI
- Jinja2
- MySQL
- HTML
- CSS
- JavaScript
- Uvicorn

## 🟡 Estrutura do Projeto
P1-DEVWEBII/ <br>
├── controller/ <br>
│ ├── controller_produto.py  <br>
│ └── controller_usuario.py  <br>
├── models/ # Modelos de dados <br>
│ ├── model_produto.py  <br> 
│ └── model_usuario.py <br>
├── templates/  <br> 
│ ├── index.html  <br>
│ ├── produtos.html <br> 
│ └── usuario.html <br>
├── venv/ <br>
├── .gitignore  <br>
├── app.py <br> 
├── main.py <br>
├── README.md <br>
└── requirements.txt

## 🟢 Como Rodar o Projeto

### Pré-Requisitos
- MySQL instalado e rodando
- Criar um banco de dados chamado 'mydb'

### Passos

1. Clonar o repositório

   ```
   git clone https://github.com/the-gabriel-marques/P1-DevWebII.git
   cd P1-DevWebII

2. Criar e Ativar o Ambiente Virtual

   ```
   python -m venv venv
   venv\scripts\activate

3. Instalar os Requerimentos

   ```
   pip install -r requirements.txt

4. Executar o Projeto (Lembre-se de criar o banco de dados 'mydb' antes)

   ```
   uvicorn main:app --reload

5. Acessar no Navegador

   ```
   http://127.0.0.1:8000/

## 🔵 Cadastro pela Interface Gráfica

![image](https://github.com/user-attachments/assets/88d4157f-732c-41f7-ab52-6983a922b4ae)

- Selecione a opção de Cadastro de Usuários

![image](https://github.com/user-attachments/assets/c21608ff-86a7-45c0-a5bd-5bfc211d8fc7)

- Preencha todos os campos

![image](https://github.com/user-attachments/assets/d9c4a6b7-cd83-4738-a240-77400ab3da0a)

- Ao preencher todos os campos corretamente, será enviado uma mensagem de confirmação

![image](https://github.com/user-attachments/assets/3c6f3554-50d9-4234-b5a8-5535764ba26d)

- Interface do Cadastro de Produtos

![image](https://github.com/user-attachments/assets/bddb7efc-24e4-45d8-93d1-2d57b39bb14b)

- Preencha todos os campos

![image](https://github.com/user-attachments/assets/9b7bedf8-d809-45fa-a252-a6a1c1c98c6a)

- Ao preencher todos os campos corretamente, será enviado uma mensagem de confirmação

## 🟣 Utilizando o PostMan

### Rotas da API para serem utilizadas

| Método | Rota              | Descrição                        | Exemplo de corpo (JSON)        |
|--------|-------------------|----------------------------------|--------------------------------|
| `GET`  | `/usuarios`       | Lista todos os usuários          | –                              |
| `GET`  | `/usuarios/{id}`  | Busca um usuário pelo ID         | –                              |
| `POST` | `/usuarios`       | Cadastra um novo usuário         | `{ "nome": "João", "email": "joao@email.com", "senha": "123456" }` |
| `PUT`  | `/usuarios/{id}`  | Atualiza os dados de um usuário  | `{ "nome": "João", "email": "joao@email.com", "senha": "nova123" }` |
| `DELETE` | `/usuarios/{id}` | Remove um usuário do sistema     | –                              |
| `GET`  | `/produtos`       | Lista todos os produtos          | –                              |
| `GET`  | `/produtos/{id}`  | Busca um produto pelo ID         | –                              |
| `POST` | `/produtos`       | Cadastra um novo produto         | `{ "nome": "Camiseta", "preco": 29.90, "estoque": 10 }` |
| `PUT`  | `/produtos/{id}`  | Atualiza os dados de um produto  | `{ "nome": "Camiseta M", "preco": 32.00, "estoque": 15 }` |
| `DELETE` | `/produtos/{id}` | Remove um produto do sistema     | –                              |

### Testes demonstrados em Imgaens

- GET (/usuarios)

![image](https://github.com/user-attachments/assets/b66ac9e5-bafc-4c26-a297-ef3968ae920e)

- GET (/usuarios/{id})

![image](https://github.com/user-attachments/assets/40bf71e5-d76b-4702-9571-611fb03c4a65)

- POST (/usuarios)

![image](https://github.com/user-attachments/assets/c09a9678-d267-4050-be01-5848bd8e8cdb)

- PUT (/usuarios/{id})

![image](https://github.com/user-attachments/assets/bbf187a1-9cbe-4c8e-b726-f52c58610db1)

- DELETE (/usaurios/{id})

![image](https://github.com/user-attachments/assets/9fd6e085-6382-49dd-8c65-e6c2bcec757f)
