import sqlite3
import tkinter as tk
# Esse arquivo só serve para iniciar a base de dados. 
# Recomendo transferir os métodos que interagem com a base de dados que estão em tela.py para cá.
# Eles só estão lá porque não sou bom em organizar essas coisas.
def conectardb():
    return sqlite3.connect('controle_medicamentos.db')
def adicionar_paciente_db(nome, idade, endereco):
    sqconnect = conectardb()
    sqcursor = sqconnect.cursor()
    sqcursor.execute('INSERT INTO pacientes (nome, idade, endereco) VALUES (?, ?, ?)', (nome, idade, endereco))
    sqconnect.commit()
    sqconnect.close()
def adicionar_medicamento_db(nome, estoque, vencimento):
    sqconnect = conectardb()
    sqcursor = sqconnect.cursor()
    sqcursor.execute('INSERT INTO medicamentos (nome, estoque, vencimento) VALUES (?, ?, ?)', (nome, estoque, vencimento))
    sqconnect.commit()
    sqconnect.close()
def carregar_pacientes_db(tree):
    sqconnect = conectardb()
    sqcursor = sqconnect.cursor()
    sqcursor.execute('SELECT nome, idade, endereco FROM pacientes')
    for row in sqcursor.fetchall(): # Peguei emprestado do código de exemplo anterior. É a mesma coisa, mas ele insere, sequencialmente, cada coluna extraída pelo fetchall().
        tree.insert("", tk.END, values=row)
        # Rachei a cabeça com isso; tkinter cria janelas que são variáveis. O treeview, por exemplo, é uma variável.
        # Mas isso significa que, se há um método que deve alterar os elementos da variável do treeview, eu preciso chamar ela como argumento do método.¹
    sqconnect.close()

def carregar_medicamentos_db(tree):
    sqconnect = conectardb()
    sqcursor = sqconnect.cursor()
    sqcursor.execute('SELECT nome, estoque, vencimento FROM medicamentos')
    for row in sqcursor.fetchall():
        tree.insert("", tk.END, values=row)
    sqconnect.close()

def gerardb():
    sqconnect = sqlite3.connect('controle_medicamentos.db') # Instanciar base de dados.
    sqcursor = sqconnect.cursor()

    # Criar tabela para pacientes (se não existir)
    sqcursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    endereco TEXT NOT NULL
                )''') # Idade deve ser integer. Oops.

    # Criar tabela para medicamentos (se não existir)
    sqcursor.execute('''CREATE TABLE IF NOT EXISTS medicamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    estoque INTEGER NOT NULL,
                    vencimento TEXT NOT NULL
                )''')

    sqconnect.commit()
    sqconnect.close()

gerardb()