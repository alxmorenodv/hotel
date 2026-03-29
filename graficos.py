import plotly.express as px
from utils import df_totaldepartamentos, graf_departamento, df_pag_mensal, df_rec_mensal, df_rec_diario


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

# FLUXO DE CAIXA MENSAL- DASHBOARD ------------------------------------------------------------------------------------------------
grafico_fluxoCaixa = px.line(
     df_rec_mensal,
     x = 'Dt_vencimento',
     y = ['Total-Receber','Total-Pagar'],
     color_discrete_sequence = ['lime','red'],
     title = 'Fluxo caixa mensal'   
 )
grafico_fluxoCaixa.update_layout(yaxis_title = 'Fluxo de Caixa Mês')
# FIM FLUXO DE CAIXA MENSAL - DASHBOARD ------------------------------------------------------------------------------------------------

# FLUXO DE CAIXA DIARIO - DASHBOARD ------------------------------------------------------------------------------------------------
grafico_fluxoCaixa_dia = px.line(
     df_rec_diario,
     x = 'Dt_vencimento',
     y = ['Total-Receber','Total-Pagar'],
     color_discrete_sequence = ['lime','red'],
     title = 'Fluxo caixa mensal'   
 )
grafico_fluxoCaixa_dia.update_layout(yaxis_title = 'Fluxo de Caixa Dia')
# FIM FLUXO DE CAIXA DIARIO - DASHBOARD ------------------------------------------------------------------------------------------------

grafico_total_departamentos = px.bar(
    graf_departamento, 
    x = 'Tipo', 
    y = 'Total',
    text_auto = True,
    title = 'Total Departamentos')