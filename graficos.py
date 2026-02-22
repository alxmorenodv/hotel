import plotly.express as px
from utils import df_totaldepartamentos, graf_departamento, df_pag_mensal, df_rec_mensal


# CONTAS A PAGAR - DASHBOARD ------------------------------------------------------------------------------------------------
grafico_pag_mensal = px.bar(
     df_pag_mensal,
     x = 'Dt_vencimento',
     y = 'Total',
     text_auto = True,
    #  range_y = (0, '100000,00'),
     color = 'Dt_vencimento',
     title = 'Contas a Pagar Mensal'   
 )
grafico_pag_mensal.update_layout(yaxis_title = 'Contas a Pagar')
# FIM CONTAS A PAGAR - DASHBOARD ------------------------------------------------------------------------------------------------

# CONTAS A RECEBER - DASHBOARD ------------------------------------------------------------------------------------------------
grafico_rec_mensal = px.bar(
     df_rec_mensal,
     x = 'Dt_vencimento',
     y = 'Total-Receber',
     text_auto = True,
    #  range_y = (0, '100000,00'),
     color = 'Dt_vencimento',
     title = 'Contas a Receber Mensal'   
 )
grafico_rec_mensal.update_layout(yaxis_title = 'Contas a Receber')
# FIM CONTAS A RECEBER - DASHBOARD ------------------------------------------------------------------------------------------------

# FLUXO DE CAIXA - DASHBOARD ------------------------------------------------------------------------------------------------
grafico_fluxoCaixa = px.line(
     df_rec_mensal,
     x = 'Dt_vencimento',
     y = ['Total-Receber','Total-Pagar'],
     color_discrete_sequence = ['lime','red'],
     title = 'Fluxo caixa mensal'   
 )
# grafico_fluxoCaixa.dd_trace(go.Scatter(x='Dt_vencimento', y='TotalPagar', mode='lines', name='TotalPagar'))
grafico_fluxoCaixa.update_layout(yaxis_title = 'Fluxo de Caixa')
# FIM FLUXO DE CAIXA- DASHBOARD ------------------------------------------------------------------------------------------------

# grafico_rec_estado = px.bar(
#     df_rec_estado.head(7),
#     x = 'Local da compra',
#     y = 'Preço',
#     text_auto = True,
#     title = 'Top Receita por Estados'
# )

# grafico_rec_categoria = px.bar(
#     df_rec_categoria.head(7),
#     text_auto = True,
#     title = 'Top 7 Categorias com Maior Receita'
# )

grafico_total_departamentos = px.bar(
    graf_departamento, 
    x = 'Tipo', 
    y = 'Total',
    text_auto = True,
    title = 'Total Departamentos')