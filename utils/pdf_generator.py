from fpdf import FPDF
import io
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Relatório de Análise de Dados", ln=True, align="C")
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

def add_section(pdf, title, content):
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, title, ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, content)
    pdf.ln(5)

def add_plot(pdf, fig, title):
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png", bbox_inches="tight", dpi=100)
    img_buffer.seek(0)
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, title, ln=True)
    pdf.ln(5)
    pdf.image(img_buffer, x=10, w=180)

def generate_pdf(data_summary, figures):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 20, "Relatório de Análise", ln=True, align="C")
    pdf.set_font("Arial", "", 14)
    pdf.cell(0, 10, f"Gerado em: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True, align="C")
    pdf.ln(20)
    add_section(pdf, "📌 Resumo", data_summary)
    for title, fig in figures.items():
        add_plot(pdf, fig, title)
    pdf_path = "relatorio.pdf"
    pdf.output(pdf_path)
    return pdf_path
