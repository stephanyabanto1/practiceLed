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

for i in range(lcd_columns):
    lcd.message(i)



# lcd.set_cursor(0,)



# def numberDemonstration():
# x = 1
# while x<10:
#     lcd.message()
#     x=x+1



# numberDemonstration()




















