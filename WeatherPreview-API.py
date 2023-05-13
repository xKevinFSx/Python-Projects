import requests
import json
import datetime
import configWeather
from geopy.geocoders import Nominatim

#Pegar localização(lat, lon) de endereço simples ou completo
geolocalizacao = Nominatim(user_agent='WeatherPreview')
print('Digite uma localização:')
localizacao = geolocalizacao.geocode(input())

#print(localizacao.address)
print(localizacao.latitude, localizacao.longitude)

#inserir os dados para acessar as infos da API
api_key = configWeather.api_key
lat = localizacao.latitude
lon = localizacao.longitude
lang = 'pt_br'
url = 'https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric&lang=%s' % (lat, lon, api_key, lang)

#chamar a API com os dados passados 
reponse = requests.get(url)

#carregar os dados para variavel
data = json.loads(reponse.text)
#print(data)

#Consumir dados via JSON da API
tempMin = data['main']['temp_min']
tempMax = data['main']['temp_max']
cidade = data['name']
dia = data['dt']
clima = data['weather'][0]['description']

#Converter data no formato GMT UNIX para padrão BR
diaConvertido = datetime.datetime.fromtimestamp(dia)
diaFormatado = diaConvertido.strftime('%d/%m/%Y')

print('Temperatura minima para ' + cidade + ' no dia ' + diaFormatado + ' é de ' + str(int(tempMin)) + '° Celsius, o tempo estará ' + clima)

print('Temperatura maxima para ' + cidade + ' no dia ' + diaFormatado + ' é de ' + str(int(tempMax)) + '° Celsius, o tempo estará ' + clima)
