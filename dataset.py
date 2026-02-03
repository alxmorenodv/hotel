# Use a biblioteca gspread para acessar diretamente o Google Sheets
# pip install gspread oauth2client
#https://www.youtube.com/watch?v=7Sy19wp0Pa8   video youtube axiliar
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
from dotenv import load_dotenv
import json

# fazendo autenticação com as credenciais do usuario google
#gc = gspread.service_account(filename="c:\\python\\credenciais.json")

load_dotenv()

credenciais = {
  "type": os.getenv("TYPE"),
  "project_id": os.getenv("PROJECT_ID"),
  "private_key_id": os.getenv("PRIVATE_KEY_ID"),
  "private_key": os.getenv("PRIVATE_KEY"),
  "client_email": os.getenv("CLIENT_EMAIL"),
  "client_id": os.getenv("CLIENT_ID"),
  "auth_uri": os.getenv("AUTH_URI"),
  "token_uri": os.getenv("TOKEN_URI"),
  "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
  "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
  "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
}

#credencialgoogle = json.dumps(os.getenv("api_google"))
#teste = json.dumps(getenv("api_google"), ident=4)
#print(credenciais)

gc = gspread.service_account_from_dict(credenciais)

# CONTAINER ------------------------------------------------------------------------------------------
# pegando os dadoscontainer da planilhacontainer online
dadoscontainer = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Yqb3QzcyV026GiwG75gw50_bMr0MV6LjNeFv10F2s44/edit?gid=0#gid=0").worksheet("lancamentos")
dadoscontainer.get_all_values()
colunascontainer = dadoscontainer.get_all_values().pop(0)

# trazendo os dadoscontainer para variavel 
planilhacontainer = pd.DataFrame(data=dadoscontainer.get_all_values(), columns=colunascontainer).drop(index=0).reset_index(drop=True)

# convertendo coluna em numeros
planilhacontainer['valor_limpo'] = planilhacontainer['Valor Total'].str.replace('R$', '', regex=False).str.strip()
planilhacontainer['Total'] = pd.to_numeric(planilhacontainer['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

# LOFT1 -----------------------------------------------------------------------------------------------
# pegando os dadoscontainer da planilhacontainer online
dadosloft1 = gc.open_by_url("https://docs.google.com/spreadsheets/d/185MABLyZHgantHGiDuPMl3t1LKbDnSlRyE6BvbBpSwc/edit?gid=0#gid=0").worksheet("lancamentos")
dadosloft1.get_all_values()
colunasloft1 = dadosloft1.get_all_values().pop(0)

# trazendo os dadoscontainer para variavel 
planilhaloft1 = pd.DataFrame(data=dadosloft1.get_all_values(), columns=colunasloft1).drop(index=0).reset_index(drop=True)

# convertendo coluna em numeros
planilhaloft1['valor_limpo'] = planilhaloft1['Valor Total'].str.replace('R$', '', regex=False).str.strip()
planilhaloft1['Total'] = pd.to_numeric(planilhaloft1['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

# LOFT2--------------------------------------------------------------------------------------------------

# pegando os dadoscontainer da planilhacontainer online
dadosloft2 = gc.open_by_url("https://docs.google.com/spreadsheets/d/1sgnJCRAdaA4tHu3ja_nTNLN0gcsKbhnf4243S-swi04/edit?gid=0#gid=0").worksheet("lancamentos")
dadosloft2.get_all_values()
colunasloft2 = dadosloft2.get_all_values().pop(0)

# trazendo os dadoscontainer para variavel 
planilhaloft2 = pd.DataFrame(data=dadosloft2.get_all_values(), columns=colunasloft2).drop(index=0).reset_index(drop=True)

# convertendo coluna em numeros
planilhaloft2['valor_limpo'] = planilhaloft2['Valor Total'].str.replace('R$', '', regex=False).str.strip()
planilhaloft2['Total'] = pd.to_numeric(planilhaloft2['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

# LOFT1 CONTAS A PAGAR -----------------------------------------------------------------------------------------------
# pegando os dados do contas a pagar da planilha do loft1 online
dadoscontaspagar = gc.open_by_url("https://docs.google.com/spreadsheets/d/185MABLyZHgantHGiDuPMl3t1LKbDnSlRyE6BvbBpSwc/edit?gid=0#gid=0").worksheet("contaspagar")
dadoscontaspagar.get_all_values()
colunascontaspagar = dadoscontaspagar.get_all_values().pop(0)

# trazendo os dadoscontainer para variavel 
planilhacontaspagar = pd.DataFrame(data=dadoscontaspagar.get_all_values(), columns=colunascontaspagar).drop(index=0).reset_index(drop=True)

# convertendo coluna em numeros
planilhacontaspagar['valor_limpo'] = planilhacontaspagar['Valor'].str.replace('R$', '', regex=False).str.strip()
planilhacontaspagar['Total'] = pd.to_numeric(planilhacontaspagar['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

#Departamentos.plot(kind="bar", x="Tipo", y="Total", title="Hotel Morenos", rot=45)
#planilhacontainer.query('Tipo == "Quartos"')
# zqdnvx388pekekakg6hbfc.streamlit.app
