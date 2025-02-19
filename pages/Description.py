import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Descrição do Projeto",
    layout="wide",
)

# Estilo customizado
st.markdown("""
    <style>
        .big-font { font-size:24px !important; font-weight: bold; color: #13610a; }
        .highlight { font-size:20px; font-weight: bold; color: #FF9800; }
        .code-font { font-size:16px; font-family: 'Courier New', monospace; }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<p class="big-font">ℹ️ Descrição do Projeto</p>', unsafe_allow_html=True)

# Descrição do projeto
st.write("""
Este projeto tem como objetivo construir um modelo preditivo para **Valor de vendas de uma empresa de Marketing baseado em seus investimento em plataformas de publicidade**.  
Para realizar a predição, o usuário deve informar o valor que deseja investir em cada plataforma, incluindo:  
""")

# Exibir características principais com emojis
st.markdown("""
✅ **Youtube**  
✅ **Facebook**  
✅ **Jornal**  
""")

st.info("ℹ️ **Nota:** A base de dados utilizada se trata de uma base fictícia e foi obtida no **ChatGPT**.")

# Visão geral do conjunto de dados
st.markdown('<p class="highlight">📊 Visão Geral dos Dados</p>', unsafe_allow_html=True)
st.write("""
O conjunto de dados consiste nas seguintes variáveis:
""")

st.table(pd.DataFrame({
    "Variável": ["Youtube", "Facebook", "Jornal","Vendas"],
    "Descrição": [
        "Investimento no Youtube",
        "Investimento no Facebook",
        "Investimento em Jornal",
        "Valor de vendas gerados"
    ]
}))

# Modelo utilizado
st.markdown('<p class="highlight">🧠 Modelo Utilizado</p>', unsafe_allow_html=True)
st.write("""
Para construir o modelo de predição do valor de vendas, foi utilizado o **LinearRegression**.  
Para definição e otimização dos hiperparâmetros foi utilizado o **GridSearchCV**, garantindo que o modelo alcançasse um melhor desempenho na previsão.  
""")

st.success("✅ **LinearRegression** foi escolhido após testes com diferentes algoritmos para garantir maior precisão.")

# Código no Streamlit
st.markdown('<p class="highlight">⚙️ Trecho de Código</p>', unsafe_allow_html=True)
# Exibir código no Streamlit
st.code("""

# Usando o GridSearchCV para encontrar o melhor modelo:    
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scale', MinMaxScaler())
])

preprocessor = ColumnTransformer([
    ('num', numerical_transformer, FEATURES)
        
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', DummyRegressor())
])

model_pipeline
        
params = {
    'model': [
        DummyRegressor(),
        LinearRegression(),
        LassoCV(),
        RidgeCV(),
        RandomForestRegressor(random_state=2023),
        GradientBoostingRegressor(random_state=2023)
    ]
}

grid_model = GridSearchCV(model_pipeline, params, cv=5, scoring='r2', verbose=1)
grid_model.fit(X_train, y_train)

# Verificando os resultados    
df_cv_results = pd.DataFrame(grid_model.cv_results_).set_index('rank_test_score').sort_index()
df_cv_results.loc[:,~df_cv_results.columns.str.contains('split|time')]
        
# Usando o GridSearchCV para encontrar os melhores parâmetros:
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

params = {
    'model__fit_intercept': [True, False],  # Se inclui ou não o intercepto
    'model__positive': [True, False],  # Se restringe os coeficientes para serem positivos
    'model__n_jobs': [None, 1, -1]  # Testa execução sequencial (None), single-thread (1) e paralela (-1)
}

grid_model = GridSearchCV(model_pipeline, params, cv=5, scoring='r2', n_jobs=-1, verbose=1)
grid_model.fit(X_train, y_train)

# Verificando os resultados    
df_cv_results = pd.DataFrame(grid_model.cv_results_).set_index('rank_test_score').sort_index()
df_cv_results.loc[:,~df_cv_results.columns.str.contains('split|time')]
       
# Definindo o melhor modelo
model_pipeline = grid_model.best_estimator_
        
# Verificando as métricas ('R2', 'MAE', 'MAPE', 'RMSE')
y_pred = model_pipeline.predict(X_test)
get_metrics(y_test, y_pred)
        
""", language="python")

st.write("""
O modelo final foi treinado utilizando os melhores hiperparâmetros encontrados, garantindo previsões mais precisas do valor das vendas.""")
