import requests
from pprint import pprint
import dotenv
import os
import streamlit as st

dotenv.load_dotenv()

token = os.environ['CHAVE_API_OPENWEATHER']

def fazer_request(url,params=None): # vou usar essa parte de código mais de uma vez 
    resposta = requests.get(url,params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f"Impossível fazer request! Erro: {e}")
        resultado = None
    else:
        resultado=resposta.json()
    return resultado

def pegar_tempo_para_local(local):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
    'appid':token,
    'q':local,
    'units':'metric',
    'lang':'pt_br',
    }
    dados_tempo = fazer_request(url=url,params=params)
    return dados_tempo

def main():
    st.title('Web App Tempo')
    st.write('Dados do OpenWeather (https://openweathermap.org/api/current)')
    local = st.text_input('Cidade que deseja buscar:')
    if not local:
        st.stop()

    dados_tempo = pegar_tempo_para_local(local=local)
    if not dados_tempo:
        st.warning(f'Dados não encontrados para a cidade {local}')
        st.stop()
    clima_atual = dados_tempo['weather'][0]['description']
    temperatura = dados_tempo['main']['temp']
    sensacao_termica = dados_tempo['main']['feels_like']
    umidade = dados_tempo['main']['humidity']
    vento = dados_tempo['wind']['speed']
    vento = vento * 3.6

    st.metric(label='Tempo atual', value=clima_atual)
    col1,col2 = st.columns(2)
    with col1:
        st.metric(label='Temperatura', value=f'{temperatura} °C')
        st.metric(label='Sensação térmica', value=f'{sensacao_termica} °C')
    with col2:
        st.metric(label='Umidade', value=f'{umidade} %')
        st.metric(label='Velocidade do vento', value=f'{vento:.2f} km/h')
    
if __name__ =='__main__':
    main()
