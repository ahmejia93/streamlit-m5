import pandas as pd
import streamlit as st

waltmart_link = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'

waltmart_data = pd.read_csv(waltmart_link)

st.title("Práctica SideBar- WaltMart USA") #Crea un título para nuestra aplicación
sidebar = st.sidebar  #  Crea una sección del lado izquierdo
sidebar.title("Esta es la barra lateral.") #Título del sidebar
sidebar.write("Aquí van los elementos de entrada.") # Párrafo explicativo del sidebar  
st.header("Descripción de los datos de WaltMart") # Subtítulo de la app

# Se despliega el dataframe
st.header("Dataset Overview")
st.dataframe(waltmart_data)

#Se configura el sidebar
state = sidebar.selectbox("State", waltmart_data['State'].unique())
category = sidebar.radio("Category", waltmart_data['Category'].unique())
subcat = sidebar.multiselect("Sub-Category", waltmart_data['Sub-Category'].unique())

st.write(""" Predicción de ventas de productos de línea blanca
 en el noroeste de los Estados Unidos 
""") # Párrafo descriptivo de la app