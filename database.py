import sqlite3

# Esse arquivo só serve para iniciar a base de dados. 
# Recomendo transferir os métodos que interagem com a base de dados que estão em tela.py para cá.
# Eles só estão lá porque não sou bom em organizar essas coisas.

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