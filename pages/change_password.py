import streamlit as st
from utils.config import supabase

st.title("🔄 Alterar Senha")

new_password = st.text_input("Nova Senha", type="password")
confirm_password = st.text_input("Confirme a Nova Senha", type="password")

if st.button("Atualizar Senha"):
    if new_password != confirm_password:
        st.error("As senhas não coincidem!")
    else:
        try:
            # Atualiza a senha do usuário usando o método de update do Supabase Auth.
            response = supabase.auth.update({"password": new_password})
            st.success("Senha atualizada com sucesso!")
            # Aqui, após atualizar, é necessário remover a flag 'password_change_required'
            # Isso pode ser feito via uma função de atualização nos metadados do usuário (depende da implementação do Supabase)
            # Exemplo (pseudo-código): supabase.from_("users").update({"user_metadata": {"password_change_required": False}}).eq("id", st.session_state["user"]["id"]).execute()
            st.experimental_rerun()
        except Exception as e:
            st.error(f"Erro ao atualizar a senha: {e}")
