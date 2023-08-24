import time
import Adafruit_CharLCD as LCD

GPIO.setwarnings(False)

#rasberry pi pin set up 

rs_pin = 25
ena_pin = 24
dB4 = 23
dB5 = 17
dB6 = 18
dB7 = 22

#initialize the pins with the 

lcd = LCD.Adafruit_CharLCD(rs_pin, ena_pin, dB4. dB5, dB6, dB7 )

lcd.message('Hello World')



