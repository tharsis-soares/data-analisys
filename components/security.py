import streamlit as st
from components.auth import get_user
from utils.config import supabase

def get_user_permissions():
    """Busca as permissões do usuário no Supabase.
       Retorna uma lista de permissões, por exemplo: ['view_reports', 'export_data']."""
    user = get_user()
    if not user:
        return []
    try:
        response = supabase.from_("permissions").select("permission").eq("user_id", user["id"]).execute()
        if response.data:
            return [p["permission"] for p in response.data]
    except Exception as e:
        st.error(f"Erro ao buscar permissões: {e}")
    return []

def require_permission(permission):
    """Decorator para restringir funções a usuários com a permissão especificada."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            permissions = get_user_permissions()
            if permission in permissions:
                return func(*args, **kwargs)
            st.error("Acesso negado. Você não tem permissão para essa ação.")
        return wrapper
    return decorator
