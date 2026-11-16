import requests
from pprint import pprint
import dotenv
import os

dotenv.load_dotenv()

token = os.environ['CHAVE_API_OPENWEATHER']

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'appid':token,
    'q':'Recife',
    'units':'metric'
}
resposta = requests.get(url=url, params=params)
try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f"Impossível fazer request! Erro: {e}")
    resultado = None
else:
    resultado=resposta.json()

pprint(resultado)