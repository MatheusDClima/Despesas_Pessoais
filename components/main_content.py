import streamlit as st
import pandas as pd
import plotly.express as px
import os

DATA_PATH = os.path.join("data", "despesas.csv")

def main_dashboard(df):
    st.subheader("Resumo de Despesas")
    total_gasto = df["Valor"].sum()
    st.metric("Total Gasto", f"R$ {total_gasto:.2f}")

    st.subheader("Gastos por Categoria")
    fig = px.pie(df, names="Categoria", values="Valor", title="Distribuição de gastos")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detalhes das Despesas")
    st.dataframe(df)
