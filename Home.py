import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Predição de valor de vendas",
    page_icon="📊",
    layout="wide",
)

# Adicionar imagem no topo da página
st.image("img/capa.png", use_column_width=True)

# Adicionando CSS para melhorar o design
st.markdown(
    """
    <style>
        /* Melhorar a seção de descrição */
        .description {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal estilizado
st.markdown('<h1 class="main-title" style="font-size: 30px; text-align: center; color: #b70a04;">📉 Modelo de Regressão para Empresa de Marketing</h1>', unsafe_allow_html=True)

# Descrição geral dentro de um bloco estilizado
st.markdown(
    """
    <div class="description">
        <p>Bem-vindo ao sistema de predição do valor de vendas!</p>
        <p>Este aplicativo permite que você insira os valores investidos em plataformas de publicidade 
        (<b>Youtube, Facebook e Jornal</b>) e preveja qual será o retorno gerado a partir desses investimentos.</p>
        <p>Utilize o menu ao lado para navegar entre as páginas:</p>
        <ul>
            <li><b>Descrição do projeto</b></li>
            <li><b>Predição do valor de vendas</b></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Adicionando um espaço em branco
st.markdown('<br>', unsafe_allow_html=True)

# Instruções básicas estilizadas
st.markdown('<h3 class="sub-title" style="font-size: 20px; color: #b70a04;">📌 Como Funciona:</h3>', unsafe_allow_html=True)
st.markdown(
    """
    <ul>
        <li><b>Home</b>: Página inicial</li>
        <li><b>Description</b>: Entenda o funcionamento do modelo e as variáveis utilizadas.</li>
        <li><b>Prediction</b>: Insira os valores dos investimentos e obtenha a previsão de vendas.</li>
    </ul>
    """,
    unsafe_allow_html=True
)
