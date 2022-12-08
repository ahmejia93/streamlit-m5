import pandas as pd
import streamlit as st

st.title('Streamlit con pandas, usando cache')
DATA_URL='/workspaces/streamlit-m5/dataset.csv'
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    return data

data_load_state = st.text('Loading..')
data = load_data(1000)
data_load_state.text('Done,(using st.cahche)')
st.dataframe(data) #Crea el DF en la app