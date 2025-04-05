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
    try:
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        return usuarios
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        return []
    finally:
        if db.is_connected():
            db.close()

def buscar_usuario_por_id(idUsuario):
    try:
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE idUsuario = %s', (idUsuario,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        print(f"Erro ao buscar usuário por ID: {e}")
        return None
    finally:
        if db.is_connected():
            db.close()

def inserir_usuario(nome, email, senha):
    try:
        db = conectar()
        cursor = db.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
        db.commit()
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
    finally:
        if db.is_connected():
            db.close()

def atualizar_usuario(idUsuario, nome, email, senha):
    try:
        db = conectar()
        cursor = db.cursor()
        cursor.execute('UPDATE usuarios SET nome=%s, email=%s, senha=%s WHERE idUsuario=%s', (nome, email, senha, idUsuario))
        db.commit()
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
    finally:
        if db.is_connected():
            db.close()

def excluir_usuario(idUsuario):
    try:
        db = conectar()
        cursor = db.cursor()
        cursor.execute('DELETE FROM usuarios WHERE idUsuario=%s', (idUsuario,))
        db.commit()
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        if db.is_connected():
            db.close()