import streamlit as st

def apply_theme():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        .main {
            background-color: #1E1E2E;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 8px 16px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #36A2EB;
        }
        .block-container {
            padding: 2rem;
        }
        .stPlotlyChart {
            border-radius: 10px;
            background-color: #282c34;
            padding: 10px;
            transition: all 0.5s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .stTitle, .stSubheader, .stPlotlyChart, .stButton, .stDataFrame {
            animation: fadeIn 0.8s ease-in-out;
        }
        </style>
    """, unsafe_allow_html=True)
