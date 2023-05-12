import requests
import json
import datetime

#inserir os dados para acessar as infos da API
api_key = 'e1889c6909b03b9d85f3e7fabd51f343'
lat = '-23.710355'
lon = '-46.495272'
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
