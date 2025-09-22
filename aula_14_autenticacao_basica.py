# Autenticação básica - construindo string "manualmente"
import base64
from pprint import pprint

import requests

url = "https://httpbin.org/basic-auth/meu-usuario/senha-secreta"

usuario = "meu-usuario"
senha = "senha-secreta"

auth_string = f'{usuario}:{senha}'.encode()  # virou bytes de UTF-8
auth_string = base64.b64encode(auth_string)  # virou bytes de b64
auth_string = auth_string.decode()  # virou string b64

print('String de autenticação final:')
print(auth_string)

headers = {
    'Authorization': f'Basic {auth_string}'
}

resposta = requests.get(url, headers=headers)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)


# Autenticação básica - utilizando HTTPBasicAuth
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/meu-usuario/senha-secreta"

usuario = "meu-usuario"
senha = "senha-secreta"
auth = HTTPBasicAuth(username=usuario, password=senha)

resposta = requests.get(url, auth=auth)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)
