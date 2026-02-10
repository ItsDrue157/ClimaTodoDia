import requests 

weather_url = "https://api.weatherapi.com/v1/current.json?key=2b8057a8e0674a46bf4144319260902&q=Rio de Janeiro&aqi=no"

try:
    response = requests.get(weather_url)
    if response.status_code == 200:
        print("Sucesso")
        conteudo = response.json()
        print('Temperatura abaixo')
        print(conteudo['current']['temp_c'])
    else:
        print("Sem Acesso")
except:
    print("Erro de conexão, verifique a internet")




