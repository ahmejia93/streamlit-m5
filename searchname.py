import streamlit as st
import pandas as pd

st.title('Streamlit - Search names')

DATA_URL='/workspaces/streamlit-m5/dataset.csv'

@st.cache
def load_data_byname(name):
    data = pd.read_csv(DATA_URL)
    #filtered_data_byname = data[data['name'].str.contains(name)] # arroja resultados que contienen la cadena en name
    filtered_data_byname = data[data['name']==name] #Seleeciona los renglones donde la búsqueda es exacta, no aproximada
    return filtered_data_byname

myname = st.text_input('Name: ')

if (myname):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0] # Gives number of rows
    st.write (f"Total names: {count_row}")
    st.dataframe(filterbyname)