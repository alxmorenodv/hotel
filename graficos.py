import plotly.express as px
from utils import df_totaldepartamentos, graf_departamento, df_pag_mensal, df_rec_mensal

# grafico_map_estado = px.scatter_geo(
#     df_rec_estado,
#     lat = 'lat',
#     lon = 'lon',
#     scope = 'south america',
#     size = 'Preço',
#     template = 'seaborn',
#     hover_name = 'Local da compra',
#     hover_data = {'lat': False, 'lon': False},
#     title = 'Receita por Estado'
# )

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
     y = 'Total',
     text_auto = True,
    #  range_y = (0, '100000,00'),
     color = 'Dt_vencimento',
     title = 'Contas a Receber Mensal'   
 )
grafico_rec_mensal.update_layout(yaxis_title = 'Contas a Receber')
# FIM CONTAS A RECEBER - DASHBOARD ------------------------------------------------------------------------------------------------

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