import RPi.GPIO as GPIO
import time

#state the variable 

LED_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


GPIO.outpput(LED_PIN, GPIO.HIGH)
time.sleep(1)

GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(1)







