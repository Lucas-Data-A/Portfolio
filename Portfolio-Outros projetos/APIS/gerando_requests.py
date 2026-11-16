import requests

url = "https://httpbin.org/get"
resposta = requests.get(url)

print(resposta.text)

#resposta em JSON
'''{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.34.2", 
    "X-Amzn-Trace-Id": "Root=1-6aa340d5-2657a3096c4d1fc93b97bc10"
  }, 
  "origin": "187.21.12.134", 
  "url": "https://httpbin.org/get"
}'''

print(resposta.json())

#Agora é um dicionário de Python com chave e valores acessíveis 
'''{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.2', 'X-Amzn-Trace-Id': 'Root=1-6aa34146-61c421c502e7beeb75f4107b'}, 'origin': '187.21.12.134', 'url': 'https://httpbin.org/get'}'''



data = {"nome":"Lucas",
 "meus_dados":[1,2,3]
}

params ={
    'DataInicio':'24-01-01',
    'DataFim':'24-02-01'
}
url = "https://httpbin.org/post"
resposta = requests.post(url, json=data,params=params)


print(resposta.json())


# resposta do post: 

'''{'args': {'DataFim': '24-02-01', 'DataInicio': '24-01-01'}, 'data': '{"nome": "Lucas", "meus_dados": [1, 2, 3]}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '42', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.2', 'X-Amzn-Trace-Id': 'Root=1-6aa344e8-5c7bb1f343fdfafc12133ac2'}, 'json': {'meus_dados': [1, 2, 3], 'nome': 'Lucas'}, 'origin': '187.21.12.134', 'url': 'https://httpbin.org/post?DataInicio=24-01-01&DataFim=24-02-01'}'''

print(resposta.request.url)

#https://httpbin.org/post?DataInicio=24-01-01&DataFim=24-02-01