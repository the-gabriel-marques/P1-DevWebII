import mysql.connector

def conectar():
    return mysql.connector.connect(host='localhost', user='root', password='', database='mydb')

def criar_tabela():
    db = conectar()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
        idProduto INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        preco DECIMAL(10,2) NOT NULL CHECK (preco > 0),
        estoque INT NOT NULL CHECK (estoque >= 0)
    )''')
    db.commit()
    db.close()

def listar_produtos():
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    db.close()
    return produtos

def buscar_produto_por_id(idProduto):
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produtos WHERE idProduto = %s', (idProduto,))
    produto = cursor.fetchone()
    db.close()
    return produto

def inserir_produto(nome, preco, estoque):
    db = conectar()
    cursor = db.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)', (nome, preco, estoque))
    db.commit()
    db.close()

def atualizar_produto(idProduto, nome, preco, estoque):
    db = conectar()
    cursor = db.cursor()
    cursor.execute('UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE idProduto=%s', (nome, preco, estoque, idProduto))
    db.commit()
    db.close()

def excluir_produto(idProduto):
    db = conectar()
    cursor = db.cursor()
    cursor.execute('DELETE FROM produtos WHERE idProduto=%s', (idProduto,))
    db.commit()
    db.close()