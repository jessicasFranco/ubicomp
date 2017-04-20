import urllib.request
import json
import os
import forecastio 
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
    #openWeatherDaily()
    #openWeatherForecast ()
    #darkSky()
    
#appkey para o openWeatherMap
appid = {"openWeather":"&appid=fc9f6c524fc093759cd28d41fda89a1b&units=metric","darkSky":"c75cdccb9021f4787ffd4802392d552c"}
files = {"DailyData":"DailyData.json","ForeCast":"ForeCast.json","darkSky":"DarkSky.json"}
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
    part = dict()
    global dt
    dt = convert_time(values["dt"])
    part[str(dt)] = values["main"]   
    save(part,files["DailyData"])   
#previsão semanal do tempo usando a api openWeatherMap
#city
#message
#list
#cod
#cnt
def openWeatherForecast ():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?lat=" + lat + "&lon=" + lon + "&lang=zh_cn"
    request = url + appid["openWeather"]
    #Open the url to read
    response =urllib.request.urlopen(request).read().decode("utf-8")
    values = json.loads(response)
    part = values["list"]
    for val in part:
        val["dt"] = str(convert_time(val["dt"]))
    save(part,files["ForeCast"])
#pervisões segundo a api darksky, retorna um json com os resultados
def darkSky(kind = list()):
    if len(kind)!= 0:
        exclude = str(kind)
        exclude = exclude[1:-1]
        exclude.replace(" ","")
        print (exclude)
        #for item in kind:
        
    url = "https://api.darksky.net/forecast/" + appid["darkSky"] + "/" + lat + "," + lon + "?exclude=flags, alerts, daily, minutely, currently"
    response = urllib.request.urlopen(url).read().decode("utf-8")
    values = json.loads(response)
    part = values["hourly"]
    part1 = part["data"]
    for item in part1:
        item["time"] = str(convert_time(item["time"]))
        print (item["time"])
    #save (values,files["darkSky"])
    #print (values)
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
def save (dataInput,file):
   if not os.path.exists(file):
       #retorna o ficheiro e o modo que pode ser usado neste caso w=writing e fecha-o
       open(file,"w").close()
   aux = []
   try:
       temp = load(file)
       for item in temp:
           aux.append(item)
   except ValueError:
       print("Empty File")
   #retorna o ficheiro e o modo que pode ser usado neste caso w=writing
   f = open (file,"w")
   #coloca os dados entre as [] do aux
   aux.append(dataInput)
   #escreve os dados do aux no ficheiro
   json.dump(aux,f,indent=3)
   #fecha o ficheiro
   f.close
#coloca os dados em lista    
def load(file):
    global lista
    with open(file) as f:
        lista = json.load(f)
        return lista      
            
#para arrancar o script automáticamente
if __name__ == "__main__": main()
#APIS
#https://apidev.accuweather.com/developers/forecastsAPIParameters
#https://github.com/ZeevG/python-forecast.io/blob/master/README.rst->darkSky Biblioteca
