import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Minha Biblioteca",
    page_icon="📚",
    layout="wide"
)

def conectar_bd():
    conexao = sqlite3.connect('biblioteca.db')
    return conexao

def buscar_livros():
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conexao.close()
    return livros

def adicionar_livro(titulo, autor, ano, genero):
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute(
            """
                INSERT INTO livros (titulo, autor, ano, genero)
                VALUES (?, ?, ?, ?);
            """,
            (titulo, autor, ano, genero)
        )
        conexao.commit()
        conexao.close()
        return True
    except Exception as e:
        st.error(f"Erro ao adicionar livro: {e}")
        return False

st.title("📚 Minha Biblioteca")

st.header("Adicionar Novo Livro")

with st.form("form_adicionar_livro", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        titulo = st.text_input("Título do Livro")
    
    with col2:
        autor = st.text_input("Autor")
    
    with col3:
        generos_opcoes = ["", "Ficção", "Fantasia", "Suspense", "Romance", "Técnico", "Não-Ficção", "Outro"]
        genero = st.selectbox("Gênero", options=generos_opcoes)

    ano = st.number_input("Ano de Publicação", step=1, format="%d", min_value=0)

    submitted = st.form_submit_button("Adicionar Livro")

if submitted:
    if titulo and autor and ano > 0 and genero:
        if adicionar_livro(titulo, autor, ano, genero):
            st.success("Livro adicionado com sucesso!")
    else:
        st.warning("Por favor, preencha todos os campos (incluindo Gênero).")


st.divider()

st.header("Livros Cadastrados")

dados_livros = buscar_livros()

if dados_livros:
    
    nomes_colunas = ['ID', 'Título', 'Autor', 'Ano', 'Gênero']
    
    df_para_exibir = pd.DataFrame(dados_livros, columns=nomes_colunas)
    
    st.dataframe(df_para_exibir, use_container_width=True)
else:
    st.write("Nenhum livro encontrado no banco de dados.")  