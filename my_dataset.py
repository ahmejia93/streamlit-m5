import pandas as pd
import streamlit as st


dataset = pd.read_csv('/workspaces/streamlit-m5/dataset.csv')
st.title('Streamlit con pandas')
st.dataframe(dataset)