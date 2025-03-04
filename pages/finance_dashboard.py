import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def plot_fluxo_caixa(df):
    # Garantir que a coluna "DATA" está no formato datetime
    df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce", format="%d/%m/%Y")

    # Remover valores nulos após a conversão de data
    df = df.dropna(subset=["DATA", "VALOR"])

    # Agrupar por data e somar valores
    fluxo = df.groupby("DATA")["VALOR"].sum()

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Definir cores para barras: Verde para valores positivos, Vermelho para negativos
    colors = ["#4CAF50" if v > 0 else "#F44336" for v in fluxo]

    fluxo.plot(kind="bar", ax=ax, color=colors, edgecolor="black")

    # Configurações visuais
    ax.set_title("Fluxo de Caixa Diário", fontsize=14, fontweight="bold")
    ax.set_xlabel("Data", fontsize=12)
    ax.set_ylabel("Valor (R$)", fontsize=12)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    ax.tick_params(axis="x", rotation=45)  # Rotacionar rótulos no eixo X para melhor leitura

    # Exibir gráfico no Streamlit
    st.pyplot(fig)

# Exemplo de uso (caso precise testar)
if "df" in locals():
    plot_fluxo_caixa(df)
