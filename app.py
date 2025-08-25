import streamlit as st
import pandas as pd
import os
from components import sidebar, main_content

# Configurações da página
st.set_page_config(page_title="Despesas Pessoais", page_icon="💰", layout="wide")
st.title("💰 Dashboard de Despesas Pessoais")

DATA_PATH = os.path.join("data", "despesas.csv")
df = pd.read_csv(DATA_PATH, parse_dates=["Data"], encoding="latin1") if os.path.exists(DATA_PATH) else pd.DataFrame(columns=["Data","Descrição","Categoria","Valor"])

# Sidebar - filtros
df_filtrado = sidebar.sidebar_filtrar(df)

# Sidebar - adicionar despesa
sidebar.sidebar_adicionar()

# Conteúdo principal
main_content.main_dashboard(df_filtrado)
