import requests

locais = {
    'itaguai': {'latitude': -22.81, 'longitude': -43.82},
    'rio': {'latitude': -22.90, 'longitude': -43.17},
    'sp': {'latitude': -23.55, 'longitude': -46.63}
}
cidade_escolhida = input("Qual cidade voce quer ver os dados? ")


url = f'https://api.open-meteo.com/v1/forecast?latitude={locais[cidade_escolhida]["latitude"]}&longitude={locais[cidade_escolhida]["longitude"]}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=1'

response = requests.get(url)

conteudo = response.json()

if cidade_escolhida in locais:
    print(f"A temperatura maxima prevista para hoje é de: {conteudo['daily']['temperature_2m_max'][0]}")
    print(f"A temperatura minima prevista para hoje é de: {conteudo['daily']['temperature_2m_min'][0]}")
    print(f"A precipitacao maxima de hoje vai ser de: {conteudo['daily']['precipitation_probability_max'][0]}%")
else:
    print("A cidade nao foi encontrada. ")













