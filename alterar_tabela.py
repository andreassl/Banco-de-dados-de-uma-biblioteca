import sqlite3

def adicionar_coluna_genero():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        # Este comando ADICIONA a nova coluna 'genero' do tipo TEXTO
        cursor.execute("ALTER TABLE livros ADD COLUMN genero TEXT")

        conexao.commit()
        conexao.close()
        print("Sucesso! A coluna 'genero' foi adicionada à tabela 'livros'.")
    except sqlite3.OperationalError as e:
        print(f"Erro (ou a coluna já existe): {e}")

# Roda a função
adicionar_coluna_genero()