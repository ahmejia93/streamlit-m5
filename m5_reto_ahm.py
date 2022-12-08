import streamlit as st
import pandas as pd

DATA_URL = ('Employees.csv')

# ENCABEZADO
st.title('Reto del Módulo 5')
st.header('Análisis del dataset de Employees')
st.write('''Este proyecto tiene por objetivo explicar el fenómeno de deserción laboral
planteado en el Hackaton HackerEarth 2020.''')
st.markdown("**Realizado por :** ***Abraham Hernández Mejía.***")
st.markdown("___")

# FUNCIONES DE PRECARGADO DE DATOS

#Cargar submuestra
@st.cache
def load_subset(nrows=500):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data
# Cargar datos completos
@st.cache
def load_cdata():
    data = pd.read_csv(DATA_URL)
    return data


# CONFIGURACIÓN DEL SIDEBAR
sidebar = st.sidebar # Se crea el sidebar
sidebar.title("Controles de tablero")
sidebar.write("Elige las opciones que quieres visualizar")
sidebar.markdown("___")

# MUESTRA DEL DATASET ORIGINAL
if sidebar.checkbox('Mostrar dataframe original'):
    st.subheader('Este es el dataset original (muestra de 500 registros). ')
    st.dataframe(load_subset()) # Se despliega el dataset en el dashboard
    st.markdown("___")


# CONFIGURACIÓN DE BUSCADOR 
@st.cache
def load_data_byfilters(employee, hometown, unit):
    data = load_cdata()
    filtered_data = data[(data['Employee_ID'].str.contains(employee)) & (data['Hometown'].str.contains(hometown)) & (data['Unit'].str.contains(unit))] # Se hace seleccion normal con pandas
    return filtered_data

st.subheader('Buscador de empleados por ciudad o unidad de trabajo')
employee_id = st.text_input('Employee ID: ') # Objetos de captura de texto
hometown = st.text_input('Hometown: ') 
unit = st.text_input('Unit: ')
btnRange = st.button('Buscar') #Objeto botón
st.markdown("___")

if (btnRange): # Si se cliclea el botón
    filterbyrange = load_data_byfilters(employee_id, hometown, unit)
    st.dataframe(filterbyrange) # Arroja el dataframe con la selección del filtro
    st.markdown("___")

# CONTADOR DE EMPLEADOS POR NIVEL EDUCATIVO
@st.cache
def load_data_byeducation(education):
    data = load_cdata()
    filtered_data_byeducation = data[data['Education_Level']==education] #Seleeciona los renglones donde la búsqueda es exacta, no aproximada
    return filtered_data_byeducation

education = sidebar.selectbox("Nivel educativo", load_cdata()['Education_Level'].sort_values().unique())

if (education):
    filterbyeducation = load_data_byeducation(education)
    count_row = filterbyeducation.shape[0] # Gives number of rows
    st.write (f"Total de registros con nivel educativo seleccionado: {count_row}")
    st.dataframe(filterbyeducation)
    st.markdown("___")

# CONTADOR DE EMPLEADOS POR CIUDAD  
@st.cache
def load_data_byhometown(hometown):
    data = load_cdata()
    filtered_data_byhometown = data[data['Hometown']==hometown] #Selecciona los renglones donde la búsqueda es exacta, no aproximada
    return filtered_data_byhometown

hometown2 = sidebar.selectbox("Ciudad", load_cdata()['Hometown'].sort_values().unique())

if (hometown2):
    filterbyhometown = load_data_byhometown(hometown2)
    count_row = filterbyhometown.shape[0] # Gives number of rows
    st.write (f"Total de registros de ciudad seleccionada: {count_row}")
    st.dataframe(filterbyhometown)
    st.markdown("___")