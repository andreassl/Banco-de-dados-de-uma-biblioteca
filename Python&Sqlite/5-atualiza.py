import sqlite3

# 1 - Conectando no BF
conexao = sqlite3.connect('netflix.db')
cursor = conexao.cursor()

# 2 - Atualiza dados
id = 1
cursor.execute(
    """
        UPDATE series SET nome = ?
        WHERE id = ?
    """,
    ("Peaky Blinders", id)
)

conexao.commit()
print("Dados atualizados!")