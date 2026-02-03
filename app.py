import streamlit as st
import plotly.express as px
from dataset import planilhacontainer
from dataset import planilhaloft1
from dataset import planilhaloft2
from dataset import planilhacontaspagar


st.set_page_config(layout='wide')
st.title("Dashboard Grupo Ideal")

# agrupando totais por departamento
departamentoscontainer = planilhacontainer.groupby("Tipo")["Total"].sum().astype(float)
departamentosloft1 = planilhaloft1.groupby("Tipo")["Total"].sum().astype(float)
departamentosloft2 = planilhaloft2.groupby("Tipo")["Total"].sum().astype(float)
departamentoscontaspagar = planilhacontaspagar.groupby("Plano-Contas")["Total"].sum().astype(float)

aba1, aba2, aba3, aba4 = st.tabs(['Hotel Container', 'Loft 1', 'Loft 2', 'Contas a Pagar'])

#https://www.udemy.com/course/desenvolvendo-dashboards-em-python/learn/lecture/38681324#overview  /etapa do curso
with aba1:
    st.dataframe(planilhacontainer, column_order=["Data", "Descrição", "Fornecedor", "Quant.", "Valor", "Valor Total", "Tipo", "Grupo"])
    
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.dataframe(departamentoscontainer)
        totalcontainer = f"R$ {planilhacontainer['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', totalcontainer)

with aba2:
    st.dataframe(planilhaloft1, column_order=["Data", "Descrição", "Fornecedor", "Quant.", "Valor", "Valor Total", "Tipo", "Grupo"])
    
    coluna21, coluna22 = st.columns(2)
    with coluna21:
        st.dataframe(departamentosloft1)
        totalloft1 = f"R$ {planilhaloft1['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', totalloft1) 
with aba3:
    st.dataframe(planilhaloft2, column_order=["Data", "Descrição", "Fornecedor", "Quant.", "Valor", "Valor Total", "Tipo", "Grupo"])

    coluna31, coluna32 = st.columns(2)
    with coluna31:
        st.dataframe(departamentosloft2)
        totalloft2 = f"R$ {planilhaloft2['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', totalloft2)     
with aba4:
    st.dataframe(planilhacontaspagar, column_order=["Data", "Vencimento", "Descrição", "Fornecedor", "Valor", "Parcela", "Plano-Contas", "Status"])

    coluna41, coluna42 = st.columns(2)
    with coluna41:
        st.subheader("Total por Departamentos")
        st.dataframe(departamentoscontaspagar)
        totalcontaspagar = f"R$ {planilhacontaspagar['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Previsto:', totalcontaspagar)



#print(departamentos)

