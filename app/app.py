import streamlit as st
import pandas as pd

df = pd.read_parquet("C:/Users/CACTU/Downloads/Proyectos/prediccion-icfes-colombia/data/procesada/icfes_analizado.parquet")




def main():
    st.title('Muestra de Datos del ICFES')
    st.header('ICFES')
    st.text("""El siguiente, es un dataframe que contiene las variables predictoras usadas para entrenar el modelo de Random Forest para Regresión.
            
El data set no está preparado aún para entrenar el modelo, es decir, no está codificado en 1 y 0 las categorías, se usa para ilustrar las variables que se usaron en el entrenamiento""")
    st.dataframe(df.head(1000))
    
main ()