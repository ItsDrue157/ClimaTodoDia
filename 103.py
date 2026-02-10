import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)
conteudo = response.json()


if response.status_code == 200:
    print(conteudo['name'] ,conteudo['email'])
    dados = {'name': conteudo['name'], 'email': conteudo['email'], 'status': 'encontrado'}
    respondePost = requests.post('https://httpbin.org/post', json=dados)
    print(respondePost.json()['json'])


else:
    print("nao foi")
