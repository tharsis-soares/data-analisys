import streamlit as st
#from dotenv import load_dotenv
from supabase import create_client, Client

#load_dotenv()  # Carrega variáveis do .env

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
