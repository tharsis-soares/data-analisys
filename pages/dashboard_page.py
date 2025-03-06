import streamlit as st
import pandas as pd

# Page title
st.title("Finance Dashboard")

# Check if data is available in session state
if 'csv_data' in st.session_state:
    df = st.session_state['csv_data']
    
    # Display the data in a table
    st.write("### Data Table")
    st.dataframe(df.head())
    
    
    if 'VALOR' in df.columns:
        df['VALOR'] = df['VALOR'].str.replace(',', '.').astype(float)
    
    # Display each column as a separate chart
    st.write("### Data Charts")
    for column in df.select_dtypes(include=['number']).columns:
        st.write(f"#### {column} Chart")
        st.line_chart(df[column])
else:
    st.warning("Please upload a CSV file on the Upload page.") 