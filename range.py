import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

DATA_URL=('/workspaces/streamlit-m5/dataset.csv')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data[(data['index']>=startid) & (data['index']<=endid)] # Se hace seleccion normal con pandas
    return filtered_data_byrange

startid = st.text_input('Start index: ') # Objetos de captura de texto
endid = st.text_input('End index: ') 
btnRange = st.button('Search by range') #Objeto botón

if (btnRange): # Si se cliclea el botón
    filterbyrange = load_data_byrange(int(startid),int(endid))
    count_row = filterbyrange.shape[0] # Otenemos el primer elemento de la tupla shape (renglones)
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyrange) # Arroja el dataframe con la selección del filtro
