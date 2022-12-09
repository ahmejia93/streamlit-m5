import streamlit as st
import pandas as pd
import plotly.express as px

#---CONFIG DE PÁGINA ---#
st.set_page_config(page_title="Análisis de employees",
                    layout='wide',
                   page_icon="👨‍🚀")

DATA_URL = ('Employees.csv')

# ENCABEZADO
st.title('Reto del Módulo 5')
st.header('Análisis del dataset de Employees')
st.write('''Este proyecto tiene por objetivo explicar el fenómeno de deserción laboral
planteado en el Hackaton HackerEarth 2020.''')
st.markdown('**Realizado por :** ***Abraham Hernández Mejía.***')
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
btnFilter = st.button('Buscar') #Objeto botón
st.markdown("___")

if (btnFilter): # Si se cliclea el botón
    filterbyparam = load_data_byfilters(employee_id, hometown, unit)
    st.dataframe(filterbyparam) # Arroja el dataframe con la selección del filtro
    st.markdown("___")

# CONTADOR DE EMPLEADOS POR NIVEL EDUCATIVO
@st.cache
def load_data_byeducation(education):
    data = load_cdata()
    filtered_data_byeducation = data[data['Education_Level']==education] #Seleeciona los renglones donde la búsqueda es exacta, no aproximada
    return filtered_data_byeducation

education = sidebar.selectbox("Nivel educativo", load_cdata()['Education_Level'].sort_values().unique())
#button_educ = sidebar.button("Filtrar y contar ")

if (education):
#if (button_educ):
    filterbyeducation = load_data_byeducation(education)
    count_row = filterbyeducation.shape[0] # Gives number of rows
    st.subheader('Filtro por nivel educativo')
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
#button_home = sidebar.button("Filtrar y contar")

if (hometown2):
#if (button_home):
    filterbyhometown = load_data_byhometown(hometown2)
    count_row = filterbyhometown.shape[0] # Gives number of rows
    st.subheader('Filtro por ciudad')
    st.write (f"Total de registros de ciudad seleccionada: {count_row}")
    st.dataframe(filterbyhometown)
    st.markdown("___")

# FILTRAR POR UNIDAD FUNCIONAL 
@st.cache
def load_data_byunit(unit):
    data = load_cdata()
    filtered_data_byunit = data[data['Unit']==unit] #Selecciona los renglones donde la búsqueda es exacta, no aproximada
    return filtered_data_byunit

st.subheader('Filtro por unidad funcional')
unit2 = st.selectbox("Unidad funcional", load_cdata()['Unit'].sort_values().unique())
#button_unit = st.button("Filtrar")

if (unit2):
#if (button_unit):
    filterbyunit = load_data_byunit(unit2)
    st.dataframe(filterbyunit)
    st.markdown("___")

# HISTOGRAMA DE EDADES
st.subheader('Histograma de edades')
#ages = load_cdata()['Age']
#fig_ages = px.histogram(ages, x="Age", nbins=10)
fig_ages = px.histogram(load_cdata()['Age'], x="Age", nbins=10,color_discrete_sequence=['#2ca5b0'])
fig_ages.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_ages)
st.markdown("**Análisis**")
st.markdown("""De acuerdo a lo que se puede observar en el histograma, el rango de edades **más común** 
es de los **20** hasta los **30 años**.""")
st.markdown("___")

# DIAGRAMA DE FRECUENCIAS UNIT
st.subheader('Diagrama de frecuencias por unidad funcional')
fig_unit = px.histogram(load_cdata()['Unit'], x="Unit", color_discrete_sequence=['#2ca5b0'])
fig_unit.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_unit)
st.markdown("**Análisis**")
st.markdown("""De acuerdo a lo que se puede observar en el diagrama, **hay más** empleados 
**en** la unidad de **IT**.""")
st.markdown("___")

# GRÁFICO DE CIUDADES CON MAYOR INDICE DE DESERCION
st.subheader('Gráfico de ciudades con mayor índice de deserción')
df=load_cdata().sort_values(by='Hometown')
selection = df[['Hometown','Attrition_rate']].groupby('Hometown').mean()
#st.dataframe(selection)

fig_cities = px.box(df, x='Hometown', y='Attrition_rate', color='Hometown')
fig_cities.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_cities)

fig_cities2 = px.bar(selection, x=selection.index, y='Attrition_rate',color=selection.index)
fig_cities2.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_cities2)

st.markdown("**Análisis**")
st.markdown("""Como se puede observar en ambos gráficos, la **variación**  en el índice deserción\
               **es mínima**, ya sea con la medida de la mediana (ver boxplot) o la medida de la\
               media (ver gráfico de barras), sin embargo, **existe una pequeña distinción** y con \
               esta misma se puede concluir que la ciudad con **mayor índice de deserción** es: **Springfield** .""")

st.markdown("___")

# GRÁFICO DE EDAD Y TASA DE DESERCIÓN 
st.subheader('Relación entre edad y tasa de deserción')
df = load_cdata()
#x_axe =df['Age']
#y_axe =df['Attrition_rate']
fig_ages_att = px.scatter(df, x=df['Age'], y=df['Attrition_rate'], color_discrete_sequence=['#2ca5b0'])
fig_ages_att.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_ages_att)

st.markdown("**Análisis**")
st.markdown("""De acuerdo a lo que se puede observar en el gráfico **no existe correlación** 
positiva o negativa entre ambas variables.""")

st.markdown("___")

# GRÁFICO DE TIEMPO DE SERVICIO Y TASA DE DESERCIÓN 
st.subheader('Relación entre tiempo de servicio y tasa de deserción')
df = load_cdata()
fig_tos_att = px.scatter(df, x=df['Time_of_service'], y=df['Attrition_rate'], color_discrete_sequence=['#2ca5b0'])
fig_tos_att.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_tos_att)

st.markdown("**Análisis**")
st.markdown("""De acuerdo a lo que se puede observar en el gráfico **no existe correlación** 
positiva o negativa entre ambas variables.""")

st.markdown("___")