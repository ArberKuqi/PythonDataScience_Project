import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Champions League Analysis⭐")
st.header("Welcome to Champions League Analysis")

uploaded_file = st.file_uploader("Choose a file",type='xlsx')

if uploaded_file is not None:
    ucl = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.write(ucl.head(10))

    st.subheader("Permbledhje e Datasetit")
    st.write(ucl.describe())

    st.subheader('Kolonat e Datasetit')
    columns = ucl.columns.tolist()
    selected_column = st.selectbox('Select a column to filter by ', columns)
    unique_values = ucl[selected_column].unique()
    selected_value = st.selectbox('Select a value to filter by ', unique_values)

    filtered_ucl = ucl[ucl[selected_column] == selected_value]
    st.write(filtered_ucl)

    st.subheader('Select Multiple Columns ')
    selected_columns = st.multiselect("Zgjedh kolonat:", ucl.columns.tolist())
    if selected_columns:
        st.dataframe(ucl[selected_columns].head(20))  # vetëm 20 rreshtat e parë për shembull
    else:
        st.info("Zgjedh se paku një kolonë për ta parë.")



else:
    st.write('Waiting on file upload...')
