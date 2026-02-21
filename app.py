import streamlit as st
import plotly.express as px
from dataset import planilhacontainer
from dataset import planilhaloft1
from dataset import planilhaloft2
from dataset import planilhacontaspagar
from utils import format_number, departamentoscontaspagar, departamentoscontainer, departamentosloft1, departamentosloft2, grupoloft1, grupoloft2, df_totaldepartamentos, graf_departamento
from graficos import grafico_total_departamentos, grafico_pag_mensal, grafico_rec_mensal

st.set_page_config(layout='wide')
st.title("Dashboard Grupo Ideal")

dash, aba1, aba2, aba3, aba4 = st.tabs(['Dashboard','Hotel Container', 'Loft 1', 'Loft 2', 'Contas a Pagar'])

#https://www.udemy.com/course/desenvolvendo-dashboards-em-python/learn/lecture/38681324#overview  /etapa do curso
with dash:
    planilhacontaspagar["Month"] = planilhacontaspagar["Dt_vencimento"].apply(lambda x: str(x.year) + "-" + str(x.month))
    month = st.sidebar.selectbox("Mês", planilhacontaspagar["Month"].unique())

    df_filtered = planilhacontaspagar[planilhacontaspagar["Month"] == month]

    st.subheader("Total Investimentos:")  
    st.metric('Total Gasto:', format_number(df_totaldepartamentos['Total'].sum(), 'R$')) 
    
    coluna1, coluna2 = st.columns(2)

    st.subheader("Contas a Pagar:") 
    st.plotly_chart(grafico_pag_mensal)

    st.subheader("Contas a Receber:") 
    st.plotly_chart(grafico_rec_mensal)

    with coluna1:
        st.dataframe(df_totaldepartamentos)
        
    with coluna2:
        st.plotly_chart(grafico_total_departamentos)
with aba1:
    st.dataframe(planilhacontainer, column_order=["Data", "Descrição", "Fornecedor", "Quant.", "Valor", "Valor Total", "Tipo", "Grupo"])
    
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.subheader("Total por Departamentos")
        st.dataframe(departamentoscontainer)
        totalcontainer = f"R$ {planilhacontainer['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', format_number(planilhacontainer['Total'].sum(), 'R$'))
    # with coluna2:
    #     st.subheader("Total por Grupo")
    #     st.dataframe(grupocontainer)
    #     totalgrupo = f"R$ {planilhacontainer['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    #     st.metric('Total Gasto:', totalgrupo)    

with aba2:
    st.dataframe(planilhaloft1, column_order=["Data", "Descrição", "Fornecedor", "Quant.", "Valor", "Valor Total", "Tipo", "Grupo"], )
    
    coluna21, coluna22, coluna23 = st.columns(3)
    with coluna21:
        st.subheader("Total por Departamentos")
        st.dataframe(departamentosloft1)
        totalloft1 = f"R$ {planilhaloft1['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        #st.metric('Total Gasto:', format_number(totalloft1, 'R$'))
        st.metric('Total Gasto:', format_number(planilhaloft1['Total'].sum(), 'R$')) 
    with coluna22:
        st.subheader("Total por Grupo")
        st.dataframe(grupoloft1)
       
    with coluna23:
        st.subheader("Total por Grupo")
        st.dataframe(grupoloft1)
     

with aba3:
    st.dataframe(planilhaloft2, column_order=["Data", "Descrição", "Fornecedor", "Quant.", "Valor", "Valor Total", "Tipo", "Grupo"])

    coluna31, coluna32 = st.columns(2)
    with coluna31:
        st.subheader("Total por Departamentos")
        st.dataframe(departamentosloft2)
        totalloft2 = f"R$ {planilhaloft2['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Gasto:', format_number(planilhaloft2['Total'].sum(), 'R$')) 
    with coluna32:
        st.subheader("Total por Grupo")
        st.dataframe(grupoloft2)
        totalgrupo = f"R$ {planilhaloft2['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")      
with aba4:
    st.dataframe(planilhacontaspagar, column_order=["Data", "Vencimento", "Descrição", "Fornecedor", "Valor", "Parcela", "Plano-Contas", "Status"])

    coluna41, coluna42 = st.columns(2)
    with coluna41:
        st.subheader("Total por Departamentos")
        st.dataframe(departamentoscontaspagar)
        totalcontaspagar = f"R$ {planilhacontaspagar['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric('Total Previsto:', totalcontaspagar)



#print(departamentos)

