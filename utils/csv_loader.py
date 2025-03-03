import pandas as pd
import streamlit as st

@st.cache_data(show_spinner="Carregando CSV...")
def load_csv(file):
    try:
        df = pd.read_csv(file)
    except Exception as e:
        st.error("Erro ao ler o CSV: " + str(e))
        return None
    return df
