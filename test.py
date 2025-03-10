import wiringpi
from wiringpi import GPIO
import time

wiringpi.wiringPiSetup()
wiringpi.pinMode(0, GPIO.OUTPUT)
while 1:
    print("ON")
    wiringpi.digitalWrite(0, GPIO.HIGH)
    time.sleep(.5)
    print("OFF")
    wiringpi.digitalWrite(0, GPIO.LOW)
    time.sleep(.5)
