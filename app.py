import streamlit as st
import plotly.express as px
import pandas as pd
from dataset import planilhacontainer
from dataset import planilhaloft1
from dataset import planilhaloft2
from dataset import planilhacontaspagar, planilhacontaspagar_pago, planilhacontaspagar_pendente, planilhacontaspagar_pago_investimento, planilhacontaspagar_pendente_investimento
from dataset import planilhaequalizacao
from utils import format_number,  grupoloft1, grupoloft2, df_totaldepartamentos
from utils import departamentoscontaspagar, departamentoscontaspagar2, departamentoscontaspagar3
from utils import departamentoscontainer, departamentosloft1, departamentosloft2
from utils import departamentoequalizacao, departamentoequalizacao2, departamentoequalizacao3
from utils import df_rec_mensal, df_rec_diario
from graficos import grafico_total_departamentos, grafico_pag_mensal, grafico_rec_mensal, grafico_fluxoCaixa, grafico_fluxoCaixa_dia

st.set_page_config(layout='wide')
st.title("Dashboard Grupo Ideal")

dash, aba1, aba2, aba3, aba4, aba5 = st.tabs(['Dashboard','Hotel Container', 'Loft 1', 'Loft 2', 'Contas a Pagar', 'Equalização'])

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

    st.subheader("Fluxo de Caixa Mensal:") 
    st.plotly_chart(grafico_fluxoCaixa)

    st.subheader("Fluxo de Caixa Diário:") 
    st.plotly_chart(grafico_fluxoCaixa_dia)

     # FLUXO CAIXA DASHBOARD -----------------------------------------------------------------------------------------------
    st.subheader("Fluxo Mês Agrupado:")  
    st.dataframe(df_rec_mensal, column_order=["Dt_vencimento", "Total-Pagar", "Total-Receber"])
    st.subheader("Fluxo Dia Agrupado:")
    st.dataframe(df_rec_diario, column_order=["Dt_vencimento", "Total-Pagar", "Total-Receber"])
    st.subheader("Total a Pagar Mês:")
    st.dataframe(df_filtered)
    # FIM FLUXO CAIXA - DASHBOARD ------------------------------------------------------------------------------------------------
  
    grafico_pag_diario = px.bar(
     df_filtered,
     x = 'Dt_vencimento',
     y = 'Total',
     text_auto = True,
    #  range_y = (0, '100000,00'),
     color = 'Dt_vencimento',
     title = 'Contas a Pagar Diario'   )
    grafico_pag_diario.update_layout(yaxis_title = 'Contas a Pagar 2')
    st.subheader("Contas a Pagar Diário:") 
    st.plotly_chart(grafico_pag_diario)

   
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
with aba4: #CONTAS A PAGAR
    coluna41, coluna42 = st.columns(2)
    with coluna41:
        totalcontaspagar_pendente = f"R$ {planilhacontaspagar_pendente['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric("TOTAL GERAL EM ABERTO:", totalcontaspagar_pendente)

        totalcontaspagar_pago = f"R$ {planilhacontaspagar_pago['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric("TOTAL PAGO:", totalcontaspagar_pago)
    with coluna42:
        totalcontaspagar_pendente_investimento = f"R$ {planilhacontaspagar_pendente_investimento['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric("TOTAL INVESTIMENTOS EM ABERTO:", totalcontaspagar_pendente_investimento)

        totalcontaspagar_pago_investimento = f"R$ {planilhacontaspagar_pago_investimento['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.metric("TOTAL PAGO INVESTIMENTOS:", totalcontaspagar_pago_investimento)

    col1, col2, col3 = st.columns(3)
    with col1:    
        st.dataframe(departamentoscontaspagar)  
    with col2:
        st.dataframe(departamentoscontaspagar2)
    with col3:
        st.dataframe(departamentoscontaspagar3)    

    st.subheader("Total em aberto")
    st.dataframe(planilhacontaspagar_pendente, column_order=["Data", "Vencimento", "Descrição", "Fornecedor", "Valor", "Parcela", "Plano-Contas", "Status"])
    st.subheader("Total pago")
    st.dataframe(planilhacontaspagar_pago, column_order=["Pagamento", "Descrição", "Fornecedor", "Valor", "Parcela", "Categoria", "Plano-Contas", "Status"])
        
        
with aba5:
    st.dataframe(planilhaequalizacao, column_order=["Data", "Vencimento", "Descrição", "Valor", "Empreendimento", "Plano-Contas", "Tipo-Pgto", "Liquidação"])
    coluna51, coluna52, coluna53 = st.columns(3)
    with coluna51:
        st.subheader("Total: ")
        totalequalizacao = f"R$ {planilhaequalizacao['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.subheader(totalequalizacao)      
        st.dataframe(departamentoequalizacao)  
    with coluna52:
        st.subheader("")
        st.subheader("")
        st.dataframe(departamentoequalizacao2)
        totalequalizacao2 = f"R$ {planilhaequalizacao['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    with coluna53:
        st.subheader("")
        st.subheader("")
        st.dataframe(departamentoequalizacao3)
        totalequalizacao3 = f"R$ {planilhaequalizacao['Total'].sum():,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")    


#print(departamentos)

