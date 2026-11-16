import requests
from pprint import pprint

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

def pegar_ids_estados(): #criar um dicionário com os estados onde a chave vai ser o id de cada estado e o valor vai ser o nome de cada estado

    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    params ={
        "view":"nivelado",
    }
    dados_estados = fazer_request(url=url,params=params)
    dict_estado = {}
    for dados in dados_estados:
        id_estado = dados['UF-id']
        nome_estado = dados['UF-nome']
        dict_estado[id_estado] = nome_estado
    return dict_estado

def pegar_frequencia_nome_estado(nome): #criar um dicionário com os estados onde a chave vai ser o id de cada estado e o valor vai ser o nome de cada estado

    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    params ={
        "groupBy":"UF",
    }
    dados_frequencias = fazer_request(url=url,params=params)
    dict_frequencias = {}
    for dados in dados_frequencias:
        id_estado = int(dados['localidade'])
        frequencia= dados['res'][0]['proporcao']
        dict_frequencias[id_estado] = frequencia
    return dict_frequencias


def main(nome):
    dict_estados = pegar_ids_estados()
    dict_frequencias = pegar_frequencia_nome_estado(nome)
    print(f'Frequencia do nome {nome} nos Estados em 100.000 habitantes')
    for id_estado, nome_estado in dict_estados.items():
        frequncia_estado = dict_frequencias[id_estado]
        print(f'->{nome_estado}: {frequncia_estado}')

if __name__ == "__main__":
    main('Lucas')