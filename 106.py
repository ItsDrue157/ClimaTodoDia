import requests
from datetime import datetime
import time

locais = {
    'itaguai': {'latitude': -22.81, 'longitude': -43.82},
    'rio': {'latitude': -22.90, 'longitude': -43.17},
    'são paulo': {'latitude': -23.55, 'longitude': -46.63}
}

cidade_escolhida = input('Qual cidade voce deseja pesquisar? ').lower() 


 



def obter_previsao(cidade_escolhida):
    dados = locais[cidade_escolhida]
    lat = dados['latitude']
    long = dados['longitude']
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=1'
    response = requests.get(url)
    conteudo = response.json()

    chuvas_max = conteudo['daily']['precipitation_probability_max'] [0]
    temp_max = conteudo['daily'] ['temperature_2m_max'] [0]
    print(f'A chance de chuva de hoje é de {chuvas_max}%')
    print(f'A temperatura maxima de hoje é de {temp_max}^')
    mensagem = f'A temperatura maxima de hoje é de {temp_max} e a A chance de chuva de hoje é de {chuvas_max}%'
    return mensagem



obter_previsao(cidade_escolhida)


