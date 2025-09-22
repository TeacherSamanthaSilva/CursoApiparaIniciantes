import os
from pprint import pprint
import sys

import dotenv
import requests
from requests.auth import HTTPBasicAuth

dotenv.load_dotenv(dotenv.find_dotenv())

# Request de autenticação
url = "https://accounts.spotify.com/api/token"

body = {
    'grant_type': 'client_credentials',
}

usuario = os.environ['SPOTIFY_CLIENT_ID']
senha = os.environ['SPOTIFY_CLIENT_SECRET']
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
