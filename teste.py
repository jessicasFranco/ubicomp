import urllib.request
import json
import pickle
import os
from datetime import datetime as dt

def main():
    coordinates = loc()
    #variavel global para a latitude
    global lat
    lat = coordinates[0]
    #variavel global para a longitude
    global lon
    lon = coordinates[1]
    global lista
    lista = list()
    openWeatherDaily()
    #openWeatherForecast ()
    
#isto é um comentário
#appkey para o openWeatherMap
appid = {"openWeather":"&appid=fc9f6c524fc093759cd28d41fda89a1b&units=metric","darkSky":"c75cdccb9021f4787ffd4802392d552c"}

#previsão do tempo diária para api openWeatherMap, retorn um ficheiro jsaon com os resultados
#informação que conseguimos obter para esta api
#clouds
#sys
#weather
#name
#dt
#main
#coord
#id
#wind
#cod
#visibility
#base
def openWeatherDaily ():
    #link responsável pelos pedidos
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon
    request = url + appid["openWeather"]
    response =urllib.request.urlopen(request).read().decode("utf-8")
    values = json.loads(response)
    part = values["main"]
    global dt
    dt = convert_time(values["dt"])
    save(part)
    
    
#previsão semanal do tempo usando a api openWeatherMap
def openWeatherForecast ():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?lat=" + lat + "&lon=" + lon + "&lang=zh_cn"
    request = url + appid["openWeather"]
    response =urllib.request.urlopen(request).read().decode("utf-8")
    values = json.loads(response)
    part = values["list"]
    for val in part:
        print(val)
    #    print (convert_time(float(val["dt"])))
        print ("\n")


#pervisões segundo a api darksky, retorna um json com os resultados
def darkSky():
    url = "https://api.darksky.net/forecast/"+ appid["darkSky"]
    
#metodo para ver as coordenadas atravez do ip, no final retorna um vector
def loc():
    url = "http://ipinfo.io/json"
    response = urllib.request.urlopen(url).read().decode("utf-8")
    values = json.loads(response)
    coordinates = values["loc"].split(",")
    return coordinates


#função para converter as datas em formato unix para formato normal    
def convert_time(date):
   return dt.fromtimestamp(date)


#função para escrever os dados num ficheiro 
def save (dataInput):
   if not os.path.exists("data.json"):
       open("data.json","w").close()
   aux = []
   try:
       temp = load()
       for item in temp:
           aux.append(item)
   except ValueError:
       print("Empty File")
   f = open ("data.json","w")
   aux.append(dataInput)
   json.dump(aux,f)
   f.close
def load():
    with open("data.json") as f:
        lista = json.load(f)
        return lista      
            
#para arrancar o script automáticamente
if __name__ == "__main__": main()
#APIS
#https://apidev.accuweather.com/developers/forecastsAPIParameters
