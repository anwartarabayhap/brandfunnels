import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📊 Brand Funnel Visualizer", layout="centered")

st.title("📈 Brand Funnel from Excel")
st.markdown("Upload your Excel file to explore brand funnel stages over time.")

# Upload Excel file
uploaded_file = st.file_uploader("📁 Upload Excel (.xls or .xlsx)", type=["xls", "xlsx"])

if uploaded_file:
    try:
        df_raw = pd.read_excel(uploaded_file, engine='xlrd')  # .xls
    except:
        df_raw = pd.read_excel(uploaded_file)  # fallback to openpyxl for .xlsx

    df = df_raw.melt(id_vars=['Brand', 'Metric'], var_name='Quarter', value_name='Value')
    df['Value'] = df['Value'].astype(str).str.replace('%', '', regex=False)
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

    brands = df['Brand'].unique()
    quarters = df['Quarter'].unique()

    col1, col2 = st.columns(2)
    selected_brand = col1.selectbox("Select Brand", brands)
    selected_quarter = col2.selectbox("Select Quarter", quarters)

    filtered = df[(df['Brand'] == selected_brand) & (df['Quarter'] == selected_quarter)]

    st.subheader(f"Funnel for {selected_brand} - {selected_quarter}")
    fig = px.funnel(filtered, x='Value', y='Metric')
    st.plotly_chart(fig, use_container_width=True)

    if st.checkbox("📈 Show trends over time"):
        trend_df = df[df['Brand'] == selected_brand]
        fig2 = px.line(trend_df, x='Quarter', y='Value', color='Metric', markers=True)
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Please upload your Excel file with columns: Brand, Metric, Q1'23, Q2'23, etc.")
