import requests
from datetime import datetime
import time
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)



def dadosDeLocalizacao(dados_recebidos):
    resultado = dados_recebidos['results'][0]
    lat = resultado['latitude']
    long = resultado['longitude']
    
    return lat,long


def clima(lat,long):
    urlLoc = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=1'
    response = requests.get(urlLoc)
    dadosClima = response.json()

    maxima = dadosClima['daily']['temperature_2m_max'] [0]
    minima = dadosClima['daily']['temperature_2m_min'][0]
    chuva = dadosClima['daily']['precipitation_probability_max'][0]

    return maxima, minima, chuva





@app.route("/bot", methods=['POST'])
def bot():
    
    
    # 1. Pegar a mensagem que o usuário enviou
    msg_usuario = request.values.get('Body', '').lower()

    
    
    # 2. Criar o objeto de resposta do Twilio
    urlGeo = f'https://geocoding-api.open-meteo.com/v1/search?name={msg_usuario}&count=1&language=pt&format=json'
    responseGeo = requests.get(urlGeo)
    conteudoGeo = responseGeo.json()

    lat, long = dadosDeLocalizacao(conteudoGeo)
    
    temperaturaMaxima, temperaturaMinima, pobraChuva = clima(lat, long)
    mensagem = (f'previsão para 📍{msg_usuario}\n'
                f'🌡️Maxima de {temperaturaMaxima}°\n'
                f'🌡️Minima de {temperaturaMinima}°\n'
                f'e a Chance de chuva é de ☔{pobraChuva}%')
    
    
    resp = MessagingResponse()
    resp.message(mensagem)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)

