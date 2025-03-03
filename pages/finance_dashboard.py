import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Painel Financeiro - Gráficos")

# 1️⃣ Fluxo de Caixa
st.subheader("Fluxo de Caixa")
fluxo_data = {
    "Data": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "Entradas": [10000, 12000, 11000, 13000, 12500, 14000, 13500, 15000, 14500, 16000, 15500, 17000],
    "Saídas":   [8000,  9000,  8500,  9500,  10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500]
}
df_fluxo = pd.DataFrame(fluxo_data)
fig_fluxo = px.line(df_fluxo, x="Data", y=["Entradas", "Saídas"], markers=True, 
                      title="Fluxo de Caixa (Entradas x Saídas)")
st.plotly_chart(fig_fluxo, use_container_width=True)

# 2️⃣ Receitas x Despesas
st.subheader("Receitas x Despesas")
rec_desp_data = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Receitas": [15000, 16000, 15500, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 20500],
    "Despesas": [12000, 12500, 12300, 13000, 12800, 13500, 13200, 13800, 14000, 14500, 14200, 14800]
}
df_recdesp = pd.DataFrame(rec_desp_data)
fig_recdesp = px.bar(df_recdesp, x="Mês", y=["Receitas", "Despesas"], barmode="group",
                     title="Receitas vs Despesas Mensais")
st.plotly_chart(fig_recdesp, use_container_width=True)

# 3️⃣ DRE (Demonstração de Resultado do Exercício)
st.subheader("DRE - Demonstração de Resultado")
dre_data = {
    "Categoria": ["Receita Bruta", "Deduções", "Receita Líquida", "Custos", 
                  "Despesas Operacionais", "Lucro Operacional", "Outras Receitas", 
                  "Outras Despesas", "Lucro Líquido"],
    "Valor": [200000, 30000, 170000, 80000, 40000, 50000, 5000, 3000, 22000]
}
df_dre = pd.DataFrame(dre_data)
fig_dre = px.pie(df_dre, names="Categoria", values="Valor", title="DRE - Distribuição dos Valores")
st.plotly_chart(fig_dre, use_container_width=True)

# 4️⃣ Inadimplência e Contas a Receber
st.subheader("Inadimplência e Contas a Receber")
inadimplencia_data = {
    "Cliente": ["Cliente A", "Cliente B", "Cliente C", "Cliente D"],
    "Valor Devido": [5000, 3000, 7000, 2000],
    "Dias de Atraso": [30, 45, 60, 15]
}
df_inadimplencia = pd.DataFrame(inadimplencia_data)
fig_inadimplencia = px.bar(df_inadimplencia, x="Cliente", y="Valor Devido", 
                           color="Dias de Atraso", text="Dias de Atraso",
                           title="Inadimplência e Contas a Receber")
st.plotly_chart(fig_inadimplencia, use_container_width=True)

# 5️⃣ Evolução do Faturamento
st.subheader("Evolução do Faturamento")
faturamento_data = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Faturamento": [14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500]
}
df_faturamento = pd.DataFrame(faturamento_data)
fig_faturamento = px.area(df_faturamento, x="Mês", y="Faturamento", 
                          title="Evolução do Faturamento", line_shape="spline")
st.plotly_chart(fig_faturamento, use_container_width=True)
