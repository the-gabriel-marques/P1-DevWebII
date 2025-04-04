import mysql.connector

def conectar():
    return mysql.connector.connect(host='localhost', user='root', password='', database='mydb')

def criar_tabela():
    db = conectar()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        idUsuario INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        senha VARCHAR(255) NOT NULL
    )''')
    db.commit()
    db.close()

def listar_usuarios():
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    db.close()
    return usuarios

def buscar_usuario_por_id(idUsuario):
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE idUsuario = %s', (idUsuario,))
    usuario = cursor.fetchone()
    db.close()
    return usuario

def inserir_usuario(nome, email, senha):
    db = conectar()
    cursor = db.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
    db.commit()
    db.close()

def atualizar_usuario(idUsuario, nome, email, senha):
    db = conectar()
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET nome=%s, email=%s, senha=%s WHERE idUsuario=%s', (nome, email, senha, idUsuario))
    db.commit()
    db.close()

def excluir_usuario(idUsuario):
    db = conectar()
    cursor = db.cursor()
    cursor.execute('DELETE FROM usuarios WHERE idUsuario=%s', (idUsuario,))
    db.commit()
    db.close()