from WearWeather import WearWeather
class Data():
    #metodo para inicializar o obj Data
    def __init__(self):
        #inicialização das vaiáveis que são necessárias para retirar o tempo
        self.wearWeather = WearWeather()
        self.wearWeatherFiles = self.wearWeather.files
        #self.forecast = self.wearWeather.load(self.wearWeatherFiles["ForeCast"])
        self.ApixuCurrent = self.wearWeather.load(self.wearWeatherFiles["ApixuCurrent"])
        #self.DarkSkyDaily = self.wearWeather.load(self.wearWeatherFiles["DarkSkyDaily"])
        self.DailyData = self.wearWeather.load(self.wearWeatherFiles["DailyData"])
        self.darkSkyCurrent = self.wearWeather.load(self.wearWeatherFiles["darkSkyCurrent"])
        self.getValues()     
    #metodo para fazer a média de todas as temperaturas
    def getValues(self):
        self.temp = 0
        self.precip_mm = 0
        self.humidity = 0
        self.pressure = 0
        self.cloud = 0
        #lista que irá ter todas as temperatutas das Apis
        temperature = list()
        #lista para a quantidade percipitação de todas as apis
        precip = list()
        #lista para as humidades
        humid = list()
        #lista para as pressoes atmosféricas
        press = list ()
        cloud_list = list()
        #para percorrer os valores retirados e da Apixu e poem na lista das temperaturas  para mais tarde fazer média
        for item in self.ApixuCurrent:
            temperature.append(item["current"]["temp_c"])
            precip.append(item["current"]["precip_mm"])
            humid.append(item["current"]["humidity"])
            press.append(item["current"]["pressure_mb"])
            cloud_list.append(item["current"]["cloud"])
        #retirar os valore das temperaturas da api openWeathermap
        for item in self.DailyData:
            temperature.append(item["temp"])
            humid.append(item["humidity"])
            press.append(item["pressure"])
        #retirar os valores das temperaturas da api darkSky
        for item in self.darkSkyCurrent:
            temperature.append(item["temperature"])
            precipIntensity = item["precipIntensity"] * 25.4  
            precip.append(precipIntensity)
            humid.append(item["humidity"]*100)
            press.append(item["pressure"])
            cloud_list.append(item["cloudCover"]*100)
        #calcular a média das temperaturas com base em todas as apis
        for item in temperature:
            self.temp += item
        #calcular a média das quantidades de precipitações
        for item in precip:
            self.precip_mm += item
        #calcular a média das humidades
        for item in humid:
            self.humidity += item
        #calcular a méda as pressoes
        for item in press:
            self.pressure += item
        #lista com as precentagens de nuvens que estam no ceu
        for item in cloud_list:
            self.cloud += item
        self.cloud = round((self.cloud/len(cloud_list)),2)
        self.pressure = round((self.pressure/len(press)),2)
        self.precip_mm = round((self.precip_mm/len(precip)),2)
        self.temp = round((self.temp/len(temperature)),2)
        self.humidity = round(self.humidity/len(humid),2)
        print ("precentagem de nuvens: ",self.cloud," %")
        print ("pressão atmosférica: ",self.pressure," mb")
        print ("percepitação: ",self.precip_mm, " mm")
        print ("temperatura: ",self.temp,"ºC")
        print ("humidade relativa:",self.humidity,"%")
