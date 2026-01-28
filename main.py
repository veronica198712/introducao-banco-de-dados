import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (?, ?)",
    ("Maria", "maria@email.com")
)

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)

conexao.commit()
conexao.close()
