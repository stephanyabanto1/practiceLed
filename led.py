import time
import Adafruit_CharLCD as LCD



# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.set_cursor(1,4)

blink = True

lcd.blink(True)

lcd.message('To tell you the truth ')

time.sleep(3)

lcd.clear()

lcd.home()


lcd.message('how are you ')













