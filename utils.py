import pandas as pd
from dataset import planilhacontainer
from dataset import planilhaloft1
from dataset import planilhaloft2
from dataset import planilhacontaspagar, planilhacontasreceber
import numpy as np

def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

# agrupando totais por departamento
departamentoscontainer = planilhacontainer.groupby("Tipo")["Total"].sum().astype(float)
departamentosloft1 = planilhaloft1.groupby("Tipo")["Total"].sum().astype(float)
departamentosloft2 = planilhaloft2.groupby("Tipo")["Total"].sum().astype(float)
departamentoscontaspagar = planilhacontaspagar.groupby("Plano-Contas")["Total"].sum().astype(float)


# AGRUPAMENTO PLANILHAS
grupoloft1 = planilhaloft1.groupby("Grupo")["Total"].sum().astype(float)
grupoloft2 = planilhaloft2.groupby("Grupo")["Total"].sum().astype(float)

df_totaldepartamentos = departamentoscontainer.add(departamentosloft1,fill_value=0).add(departamentosloft2,fill_value=0).reset_index()
graf_departamento = df_totaldepartamentos.groupby("Tipo").agg({'Total':np.sum}).reset_index()


# graf_departamento = df_totaldepartamentos.groupby("Tipo").agg({'Total':np.sum}).reset_index()
#FIM AGRUPAMENTO PLANILHAS

#df_totaldepartamentos = df_totaldep.groupby('Tipo').agg({'Total':np.mean}).sort_values('Total', ascending=False)

# # 1- Dataframe Receita por Estado
# df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
# df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# #print(df_rec_estado)

# CONTAS A PAGAR - DASHBOARD ------------------------------------------------------------------------------------------------
planilhacontaspagar['Dt_vencimento'] = pd.to_datetime(planilhacontaspagar['Vencimento'], dayfirst=True)
planilhacontaspagar['Total_limpo'] = planilhacontaspagar['Valor'].str.replace('R$', '', regex=False).str.strip()
planilhacontaspagar['Total'] = pd.to_numeric(planilhacontaspagar['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
df_pag_mensal = planilhacontaspagar.set_index('Dt_vencimento').groupby(pd.Grouper(freq='M'))['Total'].sum().reset_index()
# print(planilhacontaspagar['Total'])
# FIM CONTAS A PAGAR - DASHBOARD ------------------------------------------------------------------------------------------------

# CONTAS A RECEBER - DASHBOARD ------------------------------------------------------------------------------------------------
planilhacontasreceber['Dt_vencimento'] = pd.to_datetime(planilhacontasreceber['Vencimento'], dayfirst=True)
planilhacontasreceber['Total_limpo'] = planilhacontasreceber['Valor'].str.replace('R$', '', regex=False).str.strip()
planilhacontasreceber['Total'] = pd.to_numeric(planilhacontasreceber['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
df_rec_mensal = planilhacontasreceber.set_index('Dt_vencimento').groupby(pd.Grouper(freq='M'))['Total'].sum().reset_index()
df_rec_mensal['Total-Pagar'] = df_pag_mensal['Total'].astype(float)
df_rec_mensal['Total-Receber'] = df_rec_mensal['Total'].astype(float)
# print(df_rec_mensal)
# FIM CONTAS A RECEBER - DASHBOARD ------------------------------------------------------------------------------------------------


# fluxo_caixa = df_pag_mensal.add(df_rec_mensal,fill_value=0).reset_index()

# # 3 - Dataframe Receita por Categoria
# df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
# #print(df_rec_categoria.head())

# 4 - Dataframe Vendedores
# df_total_departamentos = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
# print(df_vendedores)