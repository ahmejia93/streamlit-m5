import streamlit as st 
  
# Crear el título para la aplicación web 
st.title("Mi Primera App con Streamlit") #Crea un título para nuestra aplicación
sidebar = st.sidebar  #  Crea una sección del lado derecho
sidebar.title("Esta es la barra lateral.") #Título del sidebar
sidebar.write("Aquí van los elementos de entrada.") # Párrafo explicativo del sidebar
st.header("Información sobre el Conjunto de Datos")  # Subtítulo dela app
  
st.header("Descripción de los datos ") # Subtítulo dela app
  
st.write(""" Este es un simple ejemplo de una app para predecir 
  
¡Esta app predice mis datos! 
""") # Párrafo descriptivo de la app