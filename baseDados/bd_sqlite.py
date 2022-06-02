import sqlite3

conexao = sqlite3.connect('learning-py/baseDados/basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50.23)
# )
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'João', 'peso': 77.12}
# )
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniel', 'peso': 68.12}
# )

# cursor.execute(
#     'UPDATE clientes SET nome = :nome WHERE id = :id',
#     {'nome': 'Fernanda', 'id': 2}
# )

# cursor.execute(
#     'DELETE FROM clientes WHERE id = :id',
#     {'id': 5}
# )

# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)

cursor.close()
conexao.close()
