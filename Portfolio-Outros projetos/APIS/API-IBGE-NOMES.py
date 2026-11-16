import requests
from pprint import pprint

nome = "ariel"
url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

params ={
    "sexo":"M",
    "localidade":"33"
}

resposta = requests.get(url,params=params)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Impossível fazer request! Erro: {e}")
else:
    print('Resultado:')
    pprint(resposta.json())

print(resposta.request.url)