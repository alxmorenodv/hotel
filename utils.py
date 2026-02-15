import pandas as pd
from dataset import planilhacontainer
from dataset import planilhaloft1
from dataset import planilhaloft2
from dataset import planilhacontaspagar
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


# agrupando totais por grupo economico
#grupocontainer = planilhacontainer.groupby("Grupo")["Total"].sum().astype(float)
grupoloft1 = planilhaloft1.groupby("Grupo")["Total"].sum().astype(float)
grupoloft2 = planilhaloft2.groupby("Grupo")["Total"].sum().astype(float)

df_totaldepartamentos = departamentoscontainer.add(departamentosloft1,fill_value=0).add(departamentosloft2,fill_value=0).reset_index()
graf_departamento = df_totaldepartamentos.groupby("Tipo").agg({'Total':np.sum}).reset_index()
#df_totaldepartamentos = df_totaldep.groupby('Tipo').agg({'Total':np.mean}).sort_values('Total', ascending=False)

# # 1- Dataframe Receita por Estado
# df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
# df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# #print(df_rec_estado)

# # 2 - Dataframe Receita Mensal
# df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
# df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
# df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()
# #print(df_rec_mensal)

# # 3 - Dataframe Receita por Categoria
# df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
# #print(df_rec_categoria.head())

# 4 - Dataframe Vendedores
# df_total_departamentos = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
# print(df_vendedores)