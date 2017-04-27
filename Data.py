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
        self.temp = 0
        self.precip_mm = 0
        self.humidity = 0
        self.getValues()     
    #metodo para fazer a média de todas as temperaturas
    def getValues(self):
        #lista que irá ter todas as temperatutas das Apis
        global temperature
        temperature = list()
        #lista para a quantida de percipitação de todas as apis
        global precip
        precip = list()
        global humid
        humid = list()
        #para percorrer os valores retirados e da Apixu e poem na lista das temperaturas  para mais tarde fazer média
        for item in self.ApixuCurrent:
            temperature.append(item["current"]["temp_c"])
            precip.append(item["current"]["precip_mm"])
            humid.append(item["current"]["humidity"])
        #retirar os valore das temperaturas da api openWeathermap
        for item in self.DailyData:
            temperature.append(item["temp"])
            humid.append(item["humidity"])
        #retirar os valores das temperaturas da api darkSky
        for item in self.darkSkyCurrent:
            temperature.append(item["temperature"])
            precipIntensity = item["precipIntensity"] * 25.4  
            precip.append(precipIntensity)
            humid.append(item["humidity"]*100)         
        #calcular a média das temperaturas com base em todas as apis
        for item in temperature:
            self.temp += item
        for item in precip:
            self.precip_mm += item
        for item in humid:
            self.humidity += item
        self.precip_mm = round((self.precip_mm/len(precip)),2)
        self.temp = round((self.temp/len(temperature)),2)
        self.humidity = round(self.humidity/len(humid),2)
        print (self.precip_mm, " mm")
        print (self.temp,"ºC")
        print (self.humidity,"%")
        
    def getPrecipAVG(self):
        print (self.darkSkyCurrent)
        
