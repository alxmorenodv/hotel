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
print(credenciais)

gc = gspread.service_account_from_dict(credenciais)

# pegando os dados da planilha online
dados = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Yqb3QzcyV026GiwG75gw50_bMr0MV6LjNeFv10F2s44/edit?gid=0#gid=0").worksheet("lancamentos")
dados.get_all_values()
colunas = dados.get_all_values().pop(0)

# trazendo os dados para variavel 
planilha = pd.DataFrame(data=dados.get_all_values(), columns=colunas).drop(index=0).reset_index(drop=True)

# convertendo coluna em numeros
planilha['valor_limpo'] = planilha['Valor Total'].str.replace('R$', '', regex=False).str.strip()
planilha['Total'] = pd.to_numeric(planilha['valor_limpo'].str.replace('.', '').str.replace(',', '.'), errors='coerce')


#Departamentos.plot(kind="bar", x="Tipo", y="Total", title="Hotel Morenos", rot=45)

#planilha.query('Tipo == "Quartos"')

# zqdnvx388pekekakg6hbfc.streamlit.app
