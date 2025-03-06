import streamlit as st
from utils.config import supabase

def get_user():
    """Retorna o usuário armazenado no session_state."""
    if "user" in st.session_state:
        return st.session_state.get("user")

def is_authenticated():
    """Verifica se há um usuário logado."""
    return get_user() is not None

def login_page():
    """Renderiza a página de login, com opções de Email/Senha e Google OAuth."""
    st.title("🔐 Login")
    option = st.radio("Escolha o método de login:", ["Email/Senha", "Google"])
    
    if option == "Email/Senha":
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            try:
                user = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state["user"] = user
                st.success("Login realizado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao fazer login: {e}")
    elif option == "Google":
        if st.button("Entrar com Google"):
            try:
                # Obtém a URL de autenticação OAuth para o Google
                url = supabase.auth.sign_in_with_oauth({"provider": "google"})
                st.markdown(f"[Clique aqui para fazer login]({url})", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro ao iniciar login com Google: {e}")

def logout():
    """Realiza logout e limpa a sessão do usuário."""
    if st.sidebar.button("Sair"):
        try:
            supabase.auth.sign_out()
        except Exception as e:
            st.error(f"Erro ao fazer logout: {e}")
        st.session_state.pop("user", None)
        st.sidebar.success("Você saiu com sucesso!")
