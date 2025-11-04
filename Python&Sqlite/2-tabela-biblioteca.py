import sqlite3


conexao = sqlite3.connect('biblioteca.db') 

cursor = conexao.cursor()


cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL
        );
    """    
)

conexao.close()
print("A tabela 'livros' foi criada")