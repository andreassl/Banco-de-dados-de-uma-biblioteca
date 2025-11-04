import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

cursor.execute(
    """
        INSERT INTO livros (titulo, autor, ano)
        VALUES ('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954);
    """
)
conexao.commit()
conexao.close()
print("Dados inseridos na tabela 'livros'")