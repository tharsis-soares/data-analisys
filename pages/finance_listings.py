import streamlit as st
import pandas as pd
import io
from fpdf import FPDF

st.title("📋 Listagens Financeiras")

# Contas a Pagar e Receber
st.subheader("Contas a Pagar e Receber")
contas_data = {
    "Fornecedor/Cliente": ["Fornecedor A", "Fornecedor B", "Cliente A", "Cliente B"],
    "Tipo": ["Pagar", "Pagar", "Receber", "Receber"],
    "Valor": [8000, 6000, 10000, 9000],
    "Vencimento": ["2023-09-10", "2023-09-15", "2023-09-20", "2023-09-25"]
}

# if "csv_data" in st.session_state:
# else:
#     print("Não há dados carregados")
    #df_contas = pd.DataFrame(contas_data)

df_contas = st.session_state["csv_data"]    
st.dataframe(df_contas)

# Despesas Fixas e Variáveis
st.subheader("Despesas Fixas e Variáveis")
despesas_data = {
    "Despesa": ["Aluguel", "Salários", "Energia", "Marketing", "Manutenção"],
    "Tipo": ["Fixa", "Fixa", "Variável", "Variável", "Variável"],
    "Valor Mensal": [3000, 12000, 800, 1500, 600]
}
df_despesas = pd.DataFrame(df_contas)
st.dataframe(df_despesas)

# Histórico de Faturamento
st.subheader("Histórico de Faturamento")
historico_data = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Faturamento": [14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500]
}
df_historico = pd.DataFrame(df_contas)
st.dataframe(df_historico)

# Exportação para Excel
st.subheader("Exportação de Relatórios")
def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Relatório")
    return output.getvalue()

excel_data = to_excel(df_contas)
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
