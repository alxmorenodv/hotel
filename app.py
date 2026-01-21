import streamlit as st
import plotly.express as px
from dataset import planilha

st.set_page_config(layout='wide')
st.title("Dashboard Grupo Ideal")

aba1, aba2, aba3 = st.tabs(['Hotel Container', 'Loft 1', 'Loft 2'])

with aba1:
    st.dataframe(planilha)

# agrupando totais por departamento
#departamentos = planilha.groupby("Tipo")["Total"].sum().astype(float)

#print(departamentos)

