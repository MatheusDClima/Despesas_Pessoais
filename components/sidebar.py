import streamlit as st
import pandas as pd
import os

DATA_PATH = os.path.join("data", "despesas.csv")

def sidebar_filtrar(df):
    st.sidebar.header("Filtros")
    categorias = df["Categoria"].dropna().unique().tolist()
    filtro_categoria = st.sidebar.multiselect(
        "Selecionar categoria", categorias, default=categorias
    )
    return df[df["Categoria"].isin(filtro_categoria)]

def sidebar_adicionar():
    st.sidebar.header("Adicionar Despesa")
    data = st.sidebar.date_input("Data")
    descricao = st.sidebar.text_input("Descrição")

    # Lê categorias existentes do CSV
    if os.path.exists(DATA_PATH):
        df_existente = pd.read_csv(DATA_PATH, encoding="latin1")
        categorias = df_existente["Categoria"].dropna().unique().tolist()
        if not categorias:
            categorias = ["Alimentação", "Transporte", "Lazer"]
    else:
        categorias = ["Alimentação", "Transporte", "Lazer"]

    # Seleção de categoria ou adição de nova
    categoria_selecionada = st.sidebar.selectbox(
        "Categoria",
        options=categorias + ["Adicionar nova..."]
    )

    if categoria_selecionada == "Adicionar nova...":
        nova_categoria = st.sidebar.text_input("Digite a nova categoria")
        if nova_categoria:
            categoria_final = nova_categoria.strip()
            if categoria_final not in categorias:
                categorias.append(categoria_final)
        else:
            categoria_final = None
    else:
        categoria_final = categoria_selecionada

    valor = st.sidebar.number_input("Valor (R$)", min_value=0.0, step=0.01)

    if st.sidebar.button("Adicionar"):
        if descricao and categoria_final and valor > 0:
            # Carrega CSV existente ou cria novo DataFrame
            df = pd.read_csv(DATA_PATH, encoding="latin1") if os.path.exists(DATA_PATH) else pd.DataFrame(columns=["Data", "Descrição", "Categoria", "Valor"])
            
            # Adiciona nova despesa
            df = pd.concat([
                df,
                pd.DataFrame([{
                    "Data": data,
                    "Descrição": descricao,
                    "Categoria": categoria_final,
                    "Valor": valor
                }])
            ], ignore_index=True)

            # Salva CSV atualizado
            df.to_csv(DATA_PATH, index=False, encoding="latin1")
            st.sidebar.success("Despesa adicionada!")
        else:
            st.sidebar.warning("Preencha todos os campos corretamente")
