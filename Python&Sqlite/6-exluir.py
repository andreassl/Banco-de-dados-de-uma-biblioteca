import sqlite3

# 1 - Conectando no BF
conexao = sqlite3.connect('netflix.db')
cursor = conexao.cursor()

# 2 - Exclusão de dados
id = 1, 2
cursor.execute(
    """
        DELETE FROM series
        WHERE id in (?, ?)
    """,
    id
)

conexao.commit()
print("Dados excluídos com sucesso")