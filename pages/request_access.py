import streamlit as st
from utils.config import supabase

st.title("Solicitação de Acesso")
st.write("Preencha os dados abaixo para solicitar acesso ao sistema.")

name = st.text_input("Nome")
email = st.text_input("Email")
message = st.text_area("Mensagem")

if st.button("Enviar Solicitação"):
    data = {"name": name, "email": email, "message": message}
    try:
        response = supabase.from_("access_requests").insert(data).execute()
        st.success("Solicitação enviada com sucesso!")
    except Exception as e:
        st.error(f"Erro ao enviar solicitação: {e}")
