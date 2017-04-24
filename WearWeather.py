import urllib.request
import json
import os
import forecastio 
from datetime import datetime as dt

class WearWeather:
    #appkey para o openWeatherMap
    appid = {"openWeather":"&appid=fc9f6c524fc093759cd28d41fda89a1b&units=metric","darkSky":"c75cdccb9021f4787ffd4802392d552c","apixu":"9b0e54aba45b4826b7c175749172004"}
    #ficheiros para gravar os dados retirados das apis
    files = {"DailyData":"DailyData.json","ForeCast":"ForeCast.json","darkSkyCurrent":"DarkSkyCurrent.json","DarkSkyDaily":"DarkSkyDaily.json","ApixuCurrent":"ApixuCurrent.json"}
    def __init__(self):
        coordinates = self.loc()
        #variavel global para a latitude
        global lat
        lat = coordinates[0]
        #variavel global para a longitude
        global lon
        lon = coordinates[1]
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
    def openWeatherDaily (self):
        #link responsável pelos pedidos
        url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon
        request = url + self.appid["openWeather"]
        response =urllib.request.urlopen(request).read().decode("utf-8")
        values = json.loads(response)
        part = dict()
        global dt
        dt = self.convert_time(values["dt"])
        part[str(dt)] = values["main"]   
        self.save(part,self.files["DailyData"])   
    #previsão semanal do tempo usando a api openWeatherMap
    #city
    #message
    #list
    #cod
    #cnt
    def openWeatherForecast (self):
        url = "http://api.openweathermap.org/data/2.5/forecast/daily?lat=" + lat + "&lon=" + lon + "&lang=zh_cn"
        request = url + self.appid["openWeather"]
        #Open the url to read
        response =urllib.request.urlopen(request).read().decode("utf-8")
        values = json.loads(response)
        part = values["list"]
        for val in part:
            val["dt"] = str(self.convert_time(val["dt"]))
        self.save(part,self.files["ForeCast"])
    #pervisões segundo a api darksky, retorna um json com os resultados
    #dá as previsões que estão momento ou um forecast dos proximos 7 dias
    def darkSky(self,kind):  
        url = "https://api.darksky.net/forecast/" + self.appid["darkSky"] + "/" + lat + "," + lon + "?exclude=" + kind + "&units=auto"
        response = urllib.request.urlopen(url).read().decode("utf-8")
        values = json.loads(response)
        #if para fazer forecasts da semana ou para o dia
        if (kind == "minutely,hourly,daily,alerts,flags"):
            #dados do tempo que se fazer sentir no momento do pedido
            part = values["currently"]
            #guardar os dados no ficheiro
            self.save (part,self.files["darkSkyCurrent"])
        elif (kind == "currently,minutely,hourly,allerts,flags"):
            #dados da previão para a semana
            part = values["daily"]["data"]
            new_part = dict()
            for item in part:
                name = str(self.convert_time(item["time"]))
                new_part[name] = item
            #guardar os dados no ficheiro
            self.save(new_part,self.files["DarkSkyDaily"])
    def apixu(self,kind):
        url = "http://api.apixu.com/v1/current.json?key=9b0e54aba45b4826b7c175749172004&q=" + lat + "," + lon
        response = urllib.request.urlopen(url).read().decode("utf-8")
        values = json.loads(response)
        del values["location"]
        self.save(values,self.files["ApixuCurrent"])

    #metodo para ver as coordenadas atravez do ip, no final retorna um vector
    def loc(self):
        url = "http://ipinfo.io/json"
        response = urllib.request.urlopen(url).read().decode("utf-8")
        values = json.loads(response)
        coordinates = values["loc"].split(",")
        return coordinates

    #função para converter as datas em formato unix para formato normal    
    def convert_time(self,date):
       return dt.fromtimestamp(date)
    #função para escrever os dados num ficheiro 
    def save (self,dataInput,file):
       if not os.path.exists(file):
           #retorna o ficheiro e o modo que pode ser usado neste caso w=writing e fecha-o
           open(file,"w").close() 
       aux = []
       try:
           temp = self.load(file)
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
    def load(self,file):
        global lista
        with open(file) as f:
            lista = json.load(f)
            return lista      
