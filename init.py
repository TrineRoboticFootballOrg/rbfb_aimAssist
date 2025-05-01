###########################################
#
# This file initializes pins, Enum types, the cv2 window, and variables used throughout
#
# Functions:
# init()
#
# Author: Caden Daffron
#
###########################################

import sys
import cv2
#import wiringpi
#from wiringpi import GPIO
from gpiozero import LED, Button


def init():
    s = 0

    global VISION_ACT_PIN
    global Tx_PIN
    VISION_ACT_PIN = 3
    Tx_PIN = 4
    #wiringpi.wiringPiSetup()
    #wiringpi.pinMode(VISION_ACT_PIN, GPIO.INPUT)
    #wiringpi.pullUpDnControl(VISION_ACT_PIN, wiringpi.PUD_DOWN)
    #wiringpi.pinMode(Tx_PIN, GPIO.OUTPUT)
    #wiringpi.digitalWrite(Tx_PIN, GPIO.HIGH)
    
    VISION_ACT_PIN = Button(23, pull_up=False)
    Tx_PIN = LED(24)
    Tx_PIN.on()


    source = cv2.VideoCapture(s)
    X_MIDLINE = int(source.get(cv2.CAP_PROP_FRAME_WIDTH))/2
    print("MID", X_MIDLINE)
    win_name = "Camera Preview"
    #cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)



    return (source, win_name, Tx_PIN, VISION_ACT_PIN, X_MIDLINE)

#init()
