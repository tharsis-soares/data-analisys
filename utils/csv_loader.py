#import pandas as pd
#import streamlit as st
#
#@st.cache_data(show_spinner="Carregando CSV...")
#def load_csv(file):
#    try:
#        df = pd.read_csv(file)
#    except Exception as e:
#        st.error("Erro ao ler o CSV: " + str(e))
#        return None
#    return df

import pandas as pd
import streamlit as st
import io

@st.cache_data(show_spinner="Carregando CSV...")
def load_csv(file):
    try:
        # Converter bytes para string
        file_content = file.getvalue().decode("utf-8")
        
        # Tentar descobrir o delimitador correto
        delimiters = [";", ",", "\t"]
        for delimiter in delimiters:
            df = pd.read_csv(io.StringIO(file_content), delimiter=delimiter, dtype=str, on_bad_lines="skip")
            if df.shape[1] > 2:  # Se tiver mais de duas colunas, provavelmente o delimitador está correto
                break

        # Renomear colunas para um formato padrão
        df.columns = ["CODIGO", "DATA", "TIPO", "DESCRICAO", "VALOR"][: len(df.columns)]
        
        # Converter a coluna "DATA" para datetime
        df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce", format="%d/%m/%Y")

        # Converter "VALOR" para número, corrigindo vírgula para ponto decimal
        df["VALOR"] = df["VALOR"].str.replace(",", ".").astype(float)

        return df.dropna()  # Remove linhas inválidas

    except Exception as e:
        st.error(f"Erro ao carregar o CSV: {e}")
        return None
