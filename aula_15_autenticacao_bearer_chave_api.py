# Autenticação com chave de API - sem dotenv
import os
from pprint import pprint

import requests

url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'Porto Alegre',
    'appid': 'SUA_CHAVE_DE_API_VAI_AQUI'
}

resposta = requests.get(url, params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    print(resposta.json())
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)


# Autenticação com chave de API - usando dotenv
# Lembre-se de editar o arquivo .env com a sua chave!
import os
from pprint import pprint

import dotenv
import requests

dotenv.load_dotenv(dotenv.find_dotenv())
app_id = os.environ['CHAVE_API_OPENWEATHER']

url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    'q': 'Porto Alegre',
    'appid': app_id,
}

resposta = requests.get(url, params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    print(resposta.json())
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)
