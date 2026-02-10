import requests

meuDados = {'name': 'Carlos', 'curso': 'Python Request'}

response = requests.post('https://httpbin.org/post', json=meuDados)

print(response.json()['json'])