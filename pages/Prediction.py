import pickle
import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(page_title='Predição')

# Titulo da página
st.markdown('<h1 style="color: #13610a;">Predição de valor das vendas</h1>', unsafe_allow_html=True)

# Descrição do projeto
st.write("""Informe o valor do investimento nas categorias abaixo:""")

# Parametros
youtube = st.number_input(label='🎥 Youtube:', value=100, min_value=0, max_value=5000)
facebook = st.number_input(label='📱 Facebook:', value=30, min_value=0, max_value=3000)
jornal = st.number_input(label='📰 Jornal:', value=50, min_value=0, max_value=1500)

# Modelo 
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def prediction():
    df_input = pd.DataFrame([{
        'youtube': youtube,
        'facebook': facebook,
        'jornal': jornal 
    }])
    prediction = model.predict(df_input)[0]
    return prediction

if st.button('Predição'):
    sales_value = prediction()
    st.success(f"Valor previsto em vendas: R$ {sales_value:.2f}")