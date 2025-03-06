
import streamlit as st
# DEVE ser a primeira instrução
st.set_page_config(page_title="DREXBPO Finance", layout="wide")

from utils.theme import apply_theme
from components.auth import is_authenticated, login_page, logout, get_user
from components.security import get_user_permissions

# Aplica o tema moderno e as animações
apply_theme()

# Se usuário estiver logado e flag password_change_required estiver True,
# força a alteração de senha antes de permitir acesso às demais páginas.
if is_authenticated():
    user = get_user()
    #if user.get("user_metadata", {}).get("password_change_required", False):
    #    with open("pages/change_password.py") as f:
    #        code = compile(f.read(), "change_password.py", "exec")
    #        exec(code)
    #    st.stop()  # Interrompe a execução até que a senha seja alterada
    if isinstance(user, dict):
        password_change_required = user.get("user_metadata", {}).get("password_change_required", False)
    else:
        # Acessa como atributo de objeto
        try:
            password_change_required = user.user_metadata.password_change_required if hasattr(user, 'user_metadata') and user.user_metadata else False
        except AttributeError:
            password_change_required = False
            
    if password_change_required:
        with open("pages/change_password.py") as f:
            code = compile(f.read(), "change_password.py", "exec")
            exec(code)
        st.stop()



# Define menu conforme autenticação
if is_authenticated():
    menu_options = ["Home", "Dashboard Financeiro", "Listagens Financeiras", "Upload de CSV", "Perfil"]
else:
    # Se não autenticado, exibe opções públicas, incluindo solicitação de acesso
    menu_options = ["Home", "Solicitar Acesso"]

st.sidebar.title("DREXBPO Finance")
page = st.sidebar.radio("Navegue:", menu_options)

if page == "Home":
    if is_authenticated():
        st.write("Bem-vindo ao DREXBPO Finance!")
    else:
        login_page()  # Exibe a página de login
elif page == "Dashboard Financeiro":
    if is_authenticated():
        with open("pages/finance_dashboard.py") as f:
            code = compile(f.read(), "finance_dashboard.py", "exec")
            exec(code)
    else:
        st.error("Acesso negado. Faça login para acessar o Dashboard.")
elif page == "Listagens Financeiras":
    if is_authenticated():
        with open("pages/finance_listings.py") as f:
            code = compile(f.read(), "finance_listings.py", "exec")
            exec(code)
    else:
        st.error("Acesso negado. Faça login para acessar as Listagens.")
elif page == "Upload de CSV":
    if is_authenticated():
        with open("pages/upload_data.py") as f:
            code = compile(f.read(), "upload_data.py", "exec")
            exec(code)
    else:
        st.error("Acesso negado. Faça login para enviar arquivos.")
elif page == "Perfil":
    if is_authenticated():
        st.title("👤 Perfil do Usuário")
        st.write("Permissões do usuário:", get_user_permissions())
    else:
        st.error("Acesso negado. Faça login para acessar seu perfil.")
elif page == "Solicitar Acesso":
    # Página pública para solicitar acesso
    with open("pages/request_access.py") as f:
        code = compile(f.read(), "request_access.py", "exec")
        exec(code)

if is_authenticated():
    logout()
