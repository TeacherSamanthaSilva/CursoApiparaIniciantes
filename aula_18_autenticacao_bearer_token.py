from pprint import pprint
import sys
import requests
from requests.auth import HTTPBasicAuth

# 🔐 Substitua pelos seus dados reais
usuario = '21d0b5af80734da2ab3f9151339c3acd'
senha = 'd49dbc8d82ef4931b55aec67c623552f'

# Request de autenticação
url = "https://accounts.spotify.com/api/token"
body = {
    'grant_type': 'client_credentials',
}
auth = HTTPBasicAuth(username=usuario, password=senha)

resposta = requests.post(url=url, data=body, auth=auth)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    token = None
else:
    token = resposta.json()['access_token']
    print('Token obtido com sucesso!')

if not token:
    sys.exit()

# Request de busca de dados
id_artista = '246dkjvS1zLTtiykXe5h60'
url = f'https://api.spotify.com/v1/artists/{id_artista}'
headers = {
    'Authorization': f'Bearer {token}'
}

resposta = requests.get(url=url, headers=headers)
pprint(resposta.json())
