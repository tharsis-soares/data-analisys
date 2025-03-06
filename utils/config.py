import streamlit as st
from supabase import create_client
from st_supabase_connection import SupabaseConnection, execute_query
# Verifica se as credenciais existem antes de carregar

st_supabase_client = st.connection(
    name="DREXBPO_FINANCE",
    type=SupabaseConnection,
    ttl=None,
    url=st.secrets["SUPABASE_URL"],
    key=st.secrets["SUPABASE_KEY"],
)

if st_supabase_client.client:
    supabase = st_supabase_client.client
else:
    st.error("⚠️ Configuração do Supabase não encontrada! Verifique o Streamlit Secrets.")
    supabase = None


#if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
#   SUPABASE_URL = st.secrets["SUPABASE_URL"]
#   SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
#   supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
#else:
#    st.error("⚠️ Configuração do Supabase não encontrada! Verifique o Streamlit Secrets.")
#    supabase = None


