import requests 

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Total de restaurantes: {len(dados)}")
    for restaurante in dados:
        print(f"- {restaurante['nome']}")
else:
    print(f"Erro ao conectar: {response.status_code}")