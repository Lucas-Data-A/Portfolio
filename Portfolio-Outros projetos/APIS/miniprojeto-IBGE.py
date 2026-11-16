import requests
from pprint import pprint

import streamlit as st
import pandas as pd

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


def pegar_nome_por_decada(nome): #criar um dicionário com os estados onde a chave vai ser o id de cada estado e o valor vai ser o nome de cada estado
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    dados_decadas = fazer_request(url=url)
    if not dados_decadas:
        return {}
    dict_decadas={}
    for dados in dados_decadas[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] = quantidade
    return dict_decadas
        

def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')

    nome = st.text_input('Consulte um nome: ')
    if not nome:
        st.stop()

    dict_decadas = pegar_nome_por_decada(nome)
    if not dict_decadas:
        st.warning(f'Nenhum dado encontrado para o nome {nome}')
        st.stop()
    df = pd.DataFrame.from_dict(dict_decadas, orient='index')
    col1,col2 = st.columns([0.3,0.7])
    with col1: 
        st.write('Frequência por decada')
        st.dataframe(df)
    with col2:
        st.write('Evolução no tempo')
        st.line_chart(df)

if __name__ == "__main__":
    main()