import streamlit as st
import plotly.express as px
from dataset import planilhacontainer
from dataset import planilhaloft1
from dataset import planilhaloft2

st.set_page_config(layout='wide')
st.title("Dashboard Grupo Ideal")

aba1, aba2, aba3 = st.tabs(['Hotel Container', 'Loft 1', 'Loft 2'])

#https://www.udemy.com/course/desenvolvendo-dashboards-em-python/learn/lecture/38681324#overview  /etapa do curso
with aba1:
    st.dataframe(planilhacontainer)

    coluna1, coluna2 = st.columns(2)
    with coluna1:
        totalcontainer = f"R$ {planilhacontainer['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', totalcontainer)  
with aba2:
    st.dataframe(planilhaloft1)

    coluna21, coluna22 = st.columns(2)
    with coluna21:
        totalloft1 = f"R$ {planilhaloft1['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', totalloft1) 
with aba3:
    st.dataframe(planilhaloft2)

    coluna31, coluna32 = st.columns(2)
    with coluna31:
        totalloft2 = f"R$ {planilhaloft2['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', totalloft2)     
      

# agrupando totais por departamento
#departamentos = planilhacontainer.groupby("Tipo")["Total"].sum().astype(float)

#print(departamentos)

