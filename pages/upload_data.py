import streamlit as st
import pandas as pd
from utils.csv_loader import load_csv

st.title("📂 Upload de CSV")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
if uploaded_file is not None:
    with st.spinner("Carregando CSV, por favor aguarde..."):
        df = load_csv(uploaded_file)
    if df is not None:
        st.session_state["csv_data"] = df
        st.success("CSV carregado com sucesso!")
        st.write("Visualização dos primeiros registros:")
        st.dataframe(df.head())
    else:
        st.error("Erro ao carregar o CSV.")
