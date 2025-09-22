# Parâmetros "sexo" e "localidade"
from pprint import pprint
import requests

url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/juliano"
params = {
    'sexo': 'M',
    'localidade': 33,
}

resposta = requests.get(url=url, params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)
print(resposta.request.url)


# Parâmetros "sexo" e "groupBy"
from pprint import pprint
import requests

url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/juliano"
params = {
    'sexo': 'M',
    'groupBy': 'UF',
}

resposta = requests.get(url=url, params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)
print(resposta.request.url)
