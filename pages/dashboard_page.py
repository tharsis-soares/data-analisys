# # # Formatação dos valores monetários
# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px

# # # Configuração da página
# # st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

# # st.title("📊 Dashboard Financeiro")

# # # Carregar dados do estado da sessão (se existirem)
# # if 'csv_data' in st.session_state:
# #     df = st.session_state['csv_data']
# # else:
# #     # Simulação de dados financeiros
# #     data = {
# #         "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
# #         "Receitas": [15000, 18000, 17000, 16000, 17500, 19000],
# #         "Despesas": [12000, 13000, 14000, 13500, 12500, 14000]
# #     }
# #     df = pd.DataFrame(data)
# #     df["Lucro"] = df["Receitas"] - df["Despesas"]

# # # Formatação dos valores monetários
# # def format_currency(value):
# #     if isinstance(value, (int, float)) and pd.notna(value):
# #         return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
# #     return "R$ 0,00"

# # for col in df.columns:
# #     if any(keyword in col.upper() for keyword in ["VALOR", "RECEITA", "DESPESA", "LUCRO"]):
# #         df[col] = df[col].apply(lambda x: format_currency(x) if isinstance(x, (int, float)) else x)


# # # Adicionar filtros dinâmicos com base nos dados
# # st.sidebar.header("Filtros")

# # # Loop through columns and create dynamic filters
# # # filters = {}
# # # for col in df.columns:
# # #     if df[col].dtype == 'object':  # Only create filters for categorical columns
# # #         unique_values = df[col].unique()
# # #         selected_values = st.sidebar.multiselect(f"Filtrar por {col}", options=unique_values, default=unique_values)
# # #         filters[col] = selected_values

# # filters = {}
# # # Loop through the columns and create filters for categorical columns only
# # for col in df.columns:
# #     if df[col].dtype == 'object':  # Only create filters for categorical columns
# #         # Get unique column names (headers) from the DataFrame
# #         unique_values = df[col].unique()
        
# #         # Create a multiselect filter for each categorical column
# #         selected_values = st.sidebar.multiselect(f"Filtrar por {col}", options=unique_values, default=unique_values)
        
# #         filters[col] = selected_values

# # # Apply the filters to the DataFrame
# # filtered_df = df
# # for col, selected_values in filters.items():
# #     filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

# # # Display the filtered table
# # st.subheader("📜 Tabela de Dados Filtrados")
# # st.dataframe(filtered_df)



# # # Apply filters to dataframe
# # filtered_df = df
# # for col, selected_values in filters.items():
# #     filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

# # # Exibir a tabela filtrada
# # st.subheader("📜 Tabela de Dados Filtrados")
# # st.dataframe(filtered_df)


# # # Dynamic Graph Selection
# # st.sidebar.header("Configuração do Gráfico")

# # # Select columns for x and y axes dynamically
# # x_axis = st.sidebar.selectbox("Escolha a coluna para o eixo X", options=df.columns)
# # y_axis = st.sidebar.selectbox("Escolha a coluna para o eixo Y", options=df.columns)

# # # Choose aggregation function
# # aggregation = st.sidebar.selectbox("Escolha a função de agregação", options=["Sum", "Mean"])

# # # Apply aggregation if needed
# # if aggregation == "Sum":
# #     graph_data = filtered_df.groupby(x_axis)[y_axis].sum().reset_index()
# # elif aggregation == "Mean":
# #     graph_data = filtered_df.groupby(x_axis)[y_axis].mean().reset_index()

# # # Create the plot
# # if y_axis != 'Valor':  # 'Valor' is already formatted as currency, avoid plotting it directly.
# #     fig_value = px.bar(graph_data, x=x_axis, y=y_axis, title=f"{aggregation} de {y_axis} por {x_axis}")
# # else:
# #     fig_value = px.bar(graph_data, x=x_axis, y=y_axis, title=f"{aggregation} de {y_axis} por {x_axis}")
    
# # st.plotly_chart(fig_value, use_container_width=True)



# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from sklearn.linear_model import LinearRegression
# import numpy as np
# from datetime import timedelta

# # ----- PAGE CONFIGURATION -----
# st.set_page_config(page_title="Dashboard Financeiro Dinâmico", layout="wide")
# st.title("📊 Dashboard Financeiro Dinâmico")

# # ----- DATA LOADING -----
# uploaded_file = st.sidebar.file_uploader("Carregar CSV", type=["csv"])
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file, delimiter=",")
# else:
#     # Sample CSV data for demonstration
#     sample_csv = """Tipo,Transferência,Id da Conta Financeira,Nome da Conta Financeira,Tipo de Repetiçao,Parcela,Quitado,Quitado Parcialmente,Conciliado,Observação/Descrição,Competência,Vencimento,Data Realizado,Data Conciliação,Valor (R$),Valor Previsto,Valor Realizado,Valor Rateio,Valor Retenção,Quantidade de Parcelas,Origem da Renegociação,Boleto Gerado,Inicial,Categoria,Departamento,Tipo Cliente/Fornecedor,Documento Cliente/Fornecedor,Cliente/Fornecedor,Numero da Nota Fiscal,Observação,Forma de Pagamento - Parcela,Forma de Pagamento - Quitação,Etiquetas,Número do Documento,Nome Vendedor,Valor PIS,Valor COFINS,Valor CSLL,Valor IRRF,Valor INSS,Valor ISS
# Despesa,Não,1,BANCO ITAU - LIBERDADE,Única,1,Sim,Não,Sim,Pagamento INPI,02/2025,03/02/2025,03/02/2025,03/02/2025,298,298,298,298,0,1,,Não,Não,Não,Taxa INPI,MATRIZ,Pessoa Juridica,42.521.088/0001-37,Instituto INPI,,,Boleto Bancário,Boleto Bancário,,149807,,
# Receita,Não,2,BANCO ITAU PENHA,Única,1,Sim,Não,Sim,REDE MAST,02/2025,03/02/2025,03/02/2025,03/02/2025,1177.87,1177.87,1177.87,1177.87,0,1,,Não,Não,Não,Pedido,FILIAIS,Pessoa Juridica,,MAST CD0091193834,,,Pix,Pix,,149808,,
# Despesa,Não,1,BANCO ITAU - LIBERDADE,Única,1,Sim,Não,Sim,Pagamento INPI,02/2025,03/02/2025,03/02/2025,03/02/2025,475,475,475,475,0,1,,Não,Não,Não,Taxa INPI,MATRIZ,Pessoa Juridica,42.521.088/0001-37,Instituto INPI,,,Boleto Bancário,Boleto Bancário,,149809,,
# Receita,Não,2,BANCO ITAU PENHA,Única,1,Sim,Não,Sim,Recebimento XYZ,02/2025,03/02/2025,03/02/2025,03/02/2025,800,800,800,800,0,1,,Não,Não,Não,Serviço,FILIAIS,Pessoa Juridica,,Cliente ABC,,,Pix,Pix,,149810,,
# Despesa,Não,1,BANCO ITAU - LIBERDADE,Única,1,Sim,Não,Sim,Pagamento INPI,02/2025,03/02/2025,03/02/2025,03/02/2025,300,300,300,300,0,1,,Não,Não,Não,Taxa INPI,MATRIZ,Pessoa Juridica,42.521.088/0001-37,Instituto INPI,,,Boleto Bancário,Boleto Bancário,,149811,,
# """
#     from io import StringIO
#     df = pd.read_csv(StringIO(sample_csv), delimiter=",")

# # Convert "Valor (R$)" to numeric (assumes dot as decimal separator)
# if df["Valor (R$)"].dtype == object:
#     df["Valor (R$)"] = df["Valor (R$)"].str.replace(",", ".").astype(float)

# # Convert "Data Realizado" to datetime
# df["Data Realizado"] = pd.to_datetime(df["Data Realizado"], dayfirst=True, errors='coerce')

# # ----- DYNAMIC FILTERING -----
# # Let user choose which header columns to filter on.
# all_columns = df.columns.tolist()
# filter_columns = st.sidebar.multiselect("Selecione as colunas para filtrar", options=all_columns, default=["Tipo", "Categoria"])
# filters = {}
# for col in filter_columns:
#     if df[col].dtype == object:
#         unique_vals = sorted(df[col].dropna().unique())
#         selected_vals = st.sidebar.multiselect(f"Filtrar por {col}", options=unique_vals, default=unique_vals)
#         filters[col] = selected_vals

# filtered_df = df.copy()
# for col, sel_vals in filters.items():
#     filtered_df = filtered_df[filtered_df[col].isin(sel_vals)]

# st.subheader("📜 Tabela de Dados Filtrados")
# st.dataframe(filtered_df)

# # ----- TABS FOR DIFFERENT VISUALIZATIONS -----
# tabs = st.tabs(["DRE", "Fluxo de Caixa", "Receitas x Despesas", "Lucro", "Projeções"])

# # ---------- TAB 1: DRE (Income Statement) ----------
# with tabs[0]:
#     st.header("Demonstração de Resultado do Exercício (DRE)")
#     total_receita = filtered_df.loc[filtered_df["Tipo"].str.lower() == "receita", "Valor (R$)"].sum()
#     total_despesa = filtered_df.loc[filtered_df["Tipo"].str.lower() == "despesa", "Valor (R$)"].sum()
#     lucro_total = total_receita - total_despesa
#     dre_data = {
#         "Métrica": ["Receita Total", "Despesa Total", "Lucro"],
#         "Valor (R$)": [total_receita, total_despesa, lucro_total]
#     }
#     dre_df = pd.DataFrame(dre_data)
#     st.table(dre_df)
#     st.markdown(f"**Lucro Total:** R$ {lucro_total:,.2f}")

# # ---------- TAB 2: Fluxo de Caixa ----------
# with tabs[1]:
#     st.header("Fluxo de Caixa")
#     receitas = filtered_df[filtered_df["Tipo"].str.lower() == "receita"]
#     despesas = filtered_df[filtered_df["Tipo"].str.lower() == "despesa"]
#     receitas_grouped = receitas.groupby("Data Realizado")["Valor (R$)"].sum().reset_index()
#     despesas_grouped = despesas.groupby("Data Realizado")["Valor (R$)"].sum().reset_index()
#     fig_fluxo = px.line(title="Fluxo de Caixa")
#     if not receitas_grouped.empty:
#         fig_fluxo.add_scatter(x=receitas_grouped["Data Realizado"], y=receitas_grouped["Valor (R$)"],
#                                 mode="lines+markers", name="Receita")
#     if not despesas_grouped.empty:
#         fig_fluxo.add_scatter(x=despesas_grouped["Data Realizado"], y=despesas_grouped["Valor (R$)"],
#                                 mode="lines+markers", name="Despesa", line=dict(dash="dash"))
#     st.plotly_chart(fig_fluxo, use_container_width=True)

# # ---------- TAB 3: Receitas x Despesas ----------
# with tabs[2]:
#     st.header("Receitas x Despesas")
#     grouped = filtered_df.groupby(["Data Realizado", "Tipo"])["Valor (R$)"].sum().reset_index()
#     fig_bar = px.bar(grouped, x="Data Realizado", y="Valor (R$)", color="Tipo",
#                      barmode="group", title="Receitas x Despesas")
#     st.plotly_chart(fig_bar, use_container_width=True)

# # ---------- TAB 4: Lucro ----------
# with tabs[3]:
#     st.header("Lucro")
#     receitas_grouped = receitas.groupby("Data Realizado")["Valor (R$)"].sum()
#     despesas_grouped = despesas.groupby("Data Realizado")["Valor (R$)"].sum()
#     lucro_series = (receitas_grouped - despesas_grouped).reset_index(name="Lucro")
#     fig_lucro = px.area(lucro_series, x="Data Realizado", y="Lucro", title="Evolução do Lucro", markers=True)
#     st.plotly_chart(fig_lucro, use_container_width=True)

# # ---------- TAB 5: Projeções ----------
# with tabs[4]:
#     st.header("Projeções")
#     st.markdown("Previsão simples usando regressão linear para o Valor Total (R$).")
#     forecast_days = st.slider("Dias para projeção", min_value=1, max_value=90, value=30)
    
#     # Aggregate total Valor (R$) by date from the filtered data
#     grouped_data = filtered_df.groupby("Data Realizado")["Valor (R$)"].sum().reset_index()
#     if len(grouped_data) >= 2:
#         grouped_data["Date_Ordinal"] = grouped_data["Data Realizado"].map(lambda d: d.toordinal())
#         X = grouped_data[["Date_Ordinal"]].values
#         y = grouped_data["Valor (R$)"].values
#         model = LinearRegression()
#         model.fit(X, y)
        
#         last_date = grouped_data["Data Realizado"].max()
#         future_dates = [last_date + timedelta(days=i) for i in range(1, forecast_days+1)]
#         future_ordinals = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
#         forecast_values = model.predict(future_ordinals)
#         forecast_df = pd.DataFrame({
#             "Data Realizado": future_dates,
#             "Forecast Valor (R$)": forecast_values
#         })
#         fig_forecast = px.line(forecast_df, x="Data Realizado", y="Forecast Valor (R$)",
#                                markers=True, title="Projeção do Valor (R$)")
#         st.plotly_chart(fig_forecast, use_container_width=True)
#     else:
#         st.warning("Dados insuficientes para projeção.")


import io
from fpdf import FPDF
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

from utils.csv_loader import load_csv

# ----- PAGE CONFIGURATION -----
st.set_page_config(page_title="Dashboard Financeiro Dinâmico", layout="wide")
st.title("📊 Dashboard Financeiro Dinâmico")

#----- DATA LOADING -----
uploaded_file = st.sidebar.file_uploader("Carregar CSV", type=["csv"])
if 'csv_data' in st.session_state:
    df = st.session_state["csv_data"]
else:
    if uploaded_file is not None:
        df_csv = load_csv(uploaded_file)
        df_csv.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
        df = df_csv.dropna(axis=1, how='all')
        df = df_csv.loc[:, ~((df_csv.fillna(0).astype(str) == "0").all(axis=0))].drop(columns=['Quantidade de Parcelas', 'Numero da Nota Fiscal', 'Nome Vendedor'])
        st.session_state["csv_data"] = df
    else:
        # Sample CSV data for demonstration
        sample_csv = """Tipo,Transferência,Id da Conta Financeira,Nome da Conta Financeira,Tipo de Repetiçao,Parcela,Quitado,Quitado Parcialmente,Conciliado,Observação/Descrição,Competência,Vencimento,Data Realizado,Data Conciliação,Valor (R$),Valor Previsto,Valor Realizado,Valor Rateio,Valor Retenção,Quantidade de Parcelas,Origem da Renegociação,Boleto Gerado,Inicial,Categoria,Departamento,Tipo Cliente/Fornecedor,Documento Cliente/Fornecedor,Cliente/Fornecedor,Numero da Nota Fiscal,Observação,Forma de Pagamento - Parcela,Forma de Pagamento - Quitação,Etiquetas,Número do Documento,Nome Vendedor,Valor PIS,Valor COFINS,Valor CSLL,Valor IRRF,Valor INSS,Valor ISS
    Despesa,Não,1,BANCO ITAU - LIBERDADE,Única,1,Sim,Não,Sim,Pagamento INPI,02/2025,03/02/2025,03/02/2025,03/02/2025,298,298,298,298,0,1,,Não,Não,Não,Taxa INPI,MATRIZ,Pessoa Juridica,42.521.088/0001-37,Instituto INPI,,,Boleto Bancário,Boleto Bancário,,149807,,
    Receita,Não,2,BANCO ITAU PENHA,Única,1,Sim,Não,Sim,REDE MAST,02/2025,03/02/2025,03/02/2025,03/02/2025,1177.87,1177.87,1177.87,1177.87,0,1,,Não,Não,Não,Pedido,FILIAIS,Pessoa Juridica,,MAST CD0091193834,,,Pix,Pix,,149808,,
    Despesa,Não,1,BANCO ITAU - LIBERDADE,Única,1,Sim,Não,Sim,Pagamento INPI,02/2025,03/02/2025,03/02/2025,03/02/2025,475,475,475,475,0,1,,Não,Não,Não,Taxa INPI,MATRIZ,Pessoa Juridica,42.521.088/0001-37,Instituto INPI,,,Boleto Bancário,Boleto Bancário,,149809,,
    Receita,Não,2,BANCO ITAU PENHA,Única,1,Sim,Não,Sim,Recebimento XYZ,02/2025,03/02/2025,03/02/2025,03/02/2025,800,800,800,800,0,1,,Não,Não,Não,Serviço,FILIAIS,Pessoa Juridica,,Cliente ABC,,,Pix,Pix,,149810,,
    Despesa,Não,1,BANCO ITAU - LIBERDADE,Única,1,Sim,Não,Sim,Pagamento INPI,02/2025,03/02/2025,03/02/2025,03/02/2025,300,300,300,300,0,1,,Não,Não,Não,Taxa INPI,MATRIZ,Pessoa Juridica,42.521.088/0001-37,Instituto INPI,,,Boleto Bancário,Boleto Bancário,,149811,,
    """
        from io import StringIO
        df = pd.read_csv(StringIO(sample_csv), delimiter=",")


# uploaded_file = st.sidebar.file_uploader("Escolha um arquivo CSV", type=["csv"])
# if 'csv_data' in st.session_state:
#     df = st.session_state["csv_data"]
# elif uploaded_file is not None:
#     with st.spinner("Carregando CSV, por favor aguarde..."):
#         df_csv = load_csv(uploaded_file)
#     if df_csv is not None:
#         df_csv.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
#         df = df_csv.dropna(axis=1, how='all')
#         df = df_csv.loc[:, ~((df_csv.fillna(0).astype(str) == "0").all(axis=0))].drop(columns=['Quantidade de Parcelas', 'Numero da Nota Fiscal', 'Nome Vendedor'])
#         st.session_state["csv_data"] = df
#         st.success("CSV carregado com sucesso!")
#         st.write("Visualização dos primeiros registros:")
#         st.dataframe(df.head())
#     else:
#         st.error("Erro ao carregar o CSV.")
    



# Convert "Valor (R$)" to numeric (assumes dot as decimal separator)
if df["Valor (R$)"].dtype == object:
    df["Valor (R$)"] = df["Valor (R$)"].str.replace(",", ".").astype(float)

# Convert "Data Realizado" to datetime
df["Data Realizado"] = pd.to_datetime(df["Data Realizado"], dayfirst=True, errors='coerce')

# ----- DYNAMIC FILTERING -----
# Let the user choose which header columns to use as filters.
all_columns = df.columns.tolist()
filter_columns = st.sidebar.multiselect("Selecione as colunas para filtrar", options=all_columns, default=["Tipo", "Categoria"])

filters = {}
for col in filter_columns:
    # For object columns, get the unique values
    column_data = df.get(col, pd.Series(dtype="object")).dropna().astype(str)

    if column_data.dtype == object:
        unique_vals = sorted(column_data.unique())
        # If there are 20 or fewer unique values, use a multiselect
        if len(unique_vals) <= 20:
            selected_vals = st.sidebar.multiselect(f"Filtrar por {col}", options=unique_vals, default=unique_vals)
            filters[col] = selected_vals
        else:
            # For columns with many unique values, use a text input to filter by substring
            search_text = st.sidebar.text_input(f"Filtrar {col} (contém)", value="")
            if search_text:
                filtered_options = [val for val in unique_vals if search_text.lower() in val.lower()]
            else:
                filtered_options = unique_vals
            # Show the (potentially smaller) list as a multiselect
            selected_vals = st.sidebar.multiselect(f"Filtrar por {col}", options=filtered_options, default=filtered_options)
            filters[col] = selected_vals

# Apply filters to the DataFrame
filtered_df = df.copy()
for col, sel_vals in filters.items():
    filtered_df = filtered_df[filtered_df[col].isin(sel_vals)]

st.subheader("📜 Tabela de Dados Filtrados")
st.dataframe(filtered_df)

# ----- TABS FOR DIFFERENT VISUALIZATIONS -----
tabs = st.tabs(["DRE", "Fluxo de Caixa", "Receitas x Despesas", "Lucro", "Projeções"])

# ---------- TAB 1: DRE (Income Statement) ----------
with tabs[0]:
    st.header("Demonstração de Resultado do Exercício (DRE)")
    total_receita = filtered_df.loc[filtered_df["Tipo"].str.lower() == "receita", "Valor (R$)"].sum()
    total_despesa = filtered_df.loc[filtered_df["Tipo"].str.lower() == "despesa", "Valor (R$)"].sum()
    lucro_total = total_receita - total_despesa
    dre_data = {
        "Métrica": ["Receita Total", "Despesa Total", "Lucro"],
        "Valor (R$)": [total_receita, total_despesa, lucro_total]
    }
    dre_df = pd.DataFrame(dre_data)
    st.table(dre_df)
    st.markdown(f"**Lucro Total:** R$ {lucro_total:,.2f}")

# ---------- TAB 2: Fluxo de Caixa ----------
with tabs[1]:
    st.header("Fluxo de Caixa")
    receitas = filtered_df[filtered_df["Tipo"].str.lower() == "receita"]
    despesas = filtered_df[filtered_df["Tipo"].str.lower() == "despesa"]
    receitas_grouped = receitas.groupby("Data Realizado")["Valor (R$)"].sum().reset_index()
    despesas_grouped = despesas.groupby("Data Realizado")["Valor (R$)"].sum().reset_index()
    fig_fluxo = px.line(title="Fluxo de Caixa")
    if not receitas_grouped.empty:
        fig_fluxo.add_scatter(x=receitas_grouped["Data Realizado"], y=receitas_grouped["Valor (R$)"],
                                mode="lines+markers", name="Receita")
    if not despesas_grouped.empty:
        fig_fluxo.add_scatter(x=despesas_grouped["Data Realizado"], y=despesas_grouped["Valor (R$)"],
                                mode="lines+markers", name="Despesa", line=dict(dash="dash"))
    st.plotly_chart(fig_fluxo, use_container_width=True)

# ---------- TAB 3: Receitas x Despesas ----------
with tabs[2]:
    st.header("Receitas x Despesas")
    grouped = filtered_df.groupby(["Data Realizado", "Tipo"])["Valor (R$)"].sum().reset_index()
    fig_bar = px.bar(grouped, x="Data Realizado", y="Valor (R$)", color="Tipo",
                     barmode="group", title="Receitas x Despesas")
    st.plotly_chart(fig_bar, use_container_width=True)

# ---------- TAB 4: Lucro ----------
with tabs[3]:
    st.header("Lucro")
    receitas_grouped = receitas.groupby("Data Realizado")["Valor (R$)"].sum()
    despesas_grouped = despesas.groupby("Data Realizado")["Valor (R$)"].sum()
    lucro_series = (receitas_grouped - despesas_grouped).reset_index(name="Lucro")
    fig_lucro = px.area(lucro_series, x="Data Realizado", y="Lucro", title="Evolução do Lucro", markers=True)
    st.plotly_chart(fig_lucro, use_container_width=True)

# ---------- TAB 5: Projeções ----------
with tabs[4]:
    st.header("Projeções")
    st.markdown("Previsão simples usando regressão linear para o Valor Total (R$).")
    forecast_days = st.slider("Dias para projeção", min_value=1, max_value=90, value=30)
    
    # Aggregate total Valor (R$) by date from the filtered data
    grouped_data = filtered_df.groupby("Data Realizado")["Valor (R$)"].sum().reset_index()
    if len(grouped_data) >= 2:
        grouped_data["Date_Ordinal"] = grouped_data["Data Realizado"].map(lambda d: d.toordinal())
        X = grouped_data[["Date_Ordinal"]].values
        y = grouped_data["Valor (R$)"].values
        model = LinearRegression()
        model.fit(X, y)
        
        last_date = grouped_data["Data Realizado"].max()
        future_dates = [last_date + timedelta(days=i) for i in range(1, forecast_days+1)]
        future_ordinals = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
        forecast_values = model.predict(future_ordinals)
        forecast_df = pd.DataFrame({
            "Data Realizado": future_dates,
            "Forecast Valor (R$)": forecast_values
        })
        fig_forecast = px.line(forecast_df, x="Data Realizado", y="Forecast Valor (R$)",
                               markers=True, title="Projeção do Valor (R$)")
        st.plotly_chart(fig_forecast, use_container_width=True)
    else:
        st.warning("Dados insuficientes para projeção.")

# Exportação para Excel
st.subheader("Exportação de Relatórios")
def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Relatório")
    return output.getvalue()

excel_data = to_excel(df)
st.download_button("Baixar Relatório Excel (Contas)", data=excel_data,
                   file_name="relatorio_contas.xlsx", mime="application/vnd.ms-excel")

# Exportação para PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Relatório Financeiro", ln=True, align="C")
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

def generate_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "Contas a Pagar e Receber:", ln=True)
    pdf.ln(5)
    # for idx, row in df_contas.iterrows():
    #     pdf.cell(0, 10, f"{row['Fornecedor/Cliente']} - {row['Tipo']} - R${row['Valor']} - Vencimento: {row['Vencimento']}", ln=True)
    pdf_file = "relatorio_financeiro.pdf"
    pdf.output(pdf_file)
    return pdf_file

if st.button("Gerar Relatório PDF"):
    pdf_file = generate_pdf()
    with open(pdf_file, "rb") as f:
        st.download_button("Baixar Relatório PDF", f, file_name=pdf_file, mime="application/pdf")