import requests

url = "https://www.google.com"

resposta = requests.get(url)

print(resposta)

#<Response [200]>: funcionou

print(resposta.text)

with open('pagina_google.html', "w") as arquivo:
    arquivo.write(resposta.text)


#A partir do request inicial no site, outros são inicializados para baixar figuras/imagens e outras coisas