# Use a biblioteca gspread para acessar diretamente o Google Sheets
# pip install gspread oauth2client
#https://www.youtube.com/watch?v=7Sy19wp0Pa8   video youtube axiliar
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib as plot
import os

# fazendo autenticação com as credenciais do usuario google
gc = gspread.service_account(filename="c:\\python\\credenciais.json")

# pegando os dados da planilha online
dados = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Yqb3QzcyV026GiwG75gw50_bMr0MV6LjNeFv10F2s44/edit?gid=0#gid=0").worksheet("lancamentos")
dados.get_all_values()
colunas = dados.get_all_values().pop(0)

# trazendo os dados para variavel 
planilha = pd.DataFrame(data=dados.get_all_values(), columns=colunas).drop(index=0).reset_index(drop=True)

# convertendo coluna em numeros
planilha['valor_limpo'] = planilha['Valor Total'].str.replace('R$', '', regex=False).str.strip()
planilha['Total'] = pd.to_numeric(planilha['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

# agrupando totais por departamento
Departamentos = planilha.groupby("Tipo")["Total"].sum().astype(float)

print(Departamentos)

Departamentos.plot(kind="bar", x="Tipo", y="Total", title="Hotel Morenos", rot=45)

planilha.query('Tipo == "Quartos"')