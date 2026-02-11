import requests
from datetime import datetime
import time

locais = {
    'itaguai': {'latitude': -22.81, 'longitude': -43.82},
    'rio de janeiro': {'latitude': -22.90, 'longitude': -43.17},
    'são paulo': {'latitude': -23.55, 'longitude': -46.63}
}

cidade_escolhida = 'itaguai' 

url = f'https://api.open-meteo.com/v1/forecast?latitude={locais[cidade_escolhida]["latitude"]}&longitude={locais[cidade_escolhida]["longitude"]}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=1'
response = requests.get(url)
conteudo = response.json() 

while True:
    horaAtual = datetime.now().hour
    if horaAtual == 23:
        if conteudo['daily']['precipitation_probability_max'] [0]>= 50:
            print("Mano pegue o guarda-chuva para nao se molhar")
        else:
            print("molhado voce nao vai ficar")
        print(f"A temperatura maxima prevista para hoje é de: {conteudo['daily']['temperature_2m_max'][0]}")
        print(f"A temperatura minima prevista para hoje é de: {conteudo['daily']['temperature_2m_min'][0]}")
        print(f"A precipitacao maxima de hoje vai ser de: {conteudo['daily']['precipitation_probability_max'][0]}%")
        
    else:
        print('programa nao esta no horario de funcionamento ')
    time.sleep(5)



    

    






    














