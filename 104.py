import requests

teste = {'lon':113.17, 'lat': 23.09}


url = f'http://www.7timer.info/bin/api.pl?lon={teste["lon"]}&lat={teste["lat"]}&product=astro&output=json'




response = requests.get(url)

conteudo = response.json()

#print(conteudo['dataseries'][0])

#print(conteudo['dataseries'][0]['temp2m'])

print(conteudo['dataseries'][2]['temp2m'])

print(conteudo ['init'])
print('temperaturas abaixo')


response = requests.get(url)
conteudo = response.json()

horaCrua = conteudo ['init'] [8:10]
horaCrua = int(horaCrua)


for item in conteudo['dataseries']:
    
    if item['timepoint'] <= 12:
        if (horaCrua + item['timepoint']) >= 24:
            print(f'Amanha:')
        horaCerta = (horaCrua + int(item['timepoint']) ) % 24
        print(f"Hora: {horaCerta} e a temperatura: {item['temp2m']}")
        



    

    

