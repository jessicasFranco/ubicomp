from Data import Data
from display import LCD
import time
import os
def start():
	a = Data()
	print (a.temp)
	b = LCD()
	while True:
		b.lcd_string("Temperature", b.LCD_LINE_1)
		b.lcd_string(str(a.temp) + u'\u00b0' +"C",b.LCD_LINE_2)
		time.sleep(3)
		b.lcd_string("Humidity", b.LCD_LINE_1)
		b.lcd_string(str(a.humidity) + "%",b.LCD_LINE_2)
		time.sleep(3)
		b.lcd_string("Precipitation", b.LCD_LINE_1)
		b.lcd_string(str(a.precip_mm) + "mm",b.LCD_LINE_2)
		time.sleep(3)
		b.lcd_string("Drink Water",b.LCD_LINE_1)
		b.lcd_string("",b.LCD_LINE_2)
		time.sleep(3)
		
		
try:		
	if __name__ == "__main__":
		start()
finally:
	print ("exit")
	os.system("rm *json")
