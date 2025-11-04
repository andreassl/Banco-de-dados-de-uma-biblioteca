import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    conexao = sqlite3.connect('biblioteca.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()
    conexao.close()
    return render_template('index.html', livros=dados)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = request.form['ano']

        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()
        cursor.execute(
            """
                INSERT INTO livros (titulo, autor, ano)
                VALUES (?, ?, ?);
            """,
            (titulo, autor, ano)
        )
        conexao.commit()
        conexao.close()

        return redirect(url_for('index'))

    return render_template('adicionar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conexao = sqlite3.connect('biblioteca.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = request.form['ano']

        cursor.execute(
            """
                UPDATE livros SET titulo = ?, autor = ?, ano = ?
                WHERE id = ?
            """,
            (titulo, autor, ano, id)
        )
        conexao.commit()
        conexao.close()

        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM livros WHERE id = ?", (id,))
        livro = cursor.fetchone()
        conexao.close()
        
        return render_template('editar.html', livro=livro)

@app.route('/excluir/<int:id>')
def excluir(id):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)