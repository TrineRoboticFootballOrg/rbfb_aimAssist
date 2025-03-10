import sys
import cv2
import wiringpi
from wiringpi import GPIO
from imutils.video import FPS
from enum import Enum

class filter_mode(Enum):
	PREVIEW  = 0
	BLUR     = 1
	HSV      = 2

class algo_sel(Enum):
	FEATURE  = 0
	CANNY    = 1
	
def init():
    s = 0

    global VISION_ACT_PIN
    global TURN_LEFT_PIN
    global TURN_RIGHT_PIN
    VISION_ACT_PIN = 0
    TURN_LEFT_PIN = 1
    TURN_RIGHT_PIN = 2
    wiringpi.wiringPiSetup()
    print("VISIONACTPIN", VISION_ACT_PIN)
    wiringpi.pinMode(VISION_ACT_PIN, GPIO.INPUT)
    wiringpi.pullUpDnControl(VISION_ACT_PIN, wiringpi.PUD_UP)
    wiringpi.pinMode(TURN_LEFT_PIN, GPIO.OUTPUT)
    wiringpi.digitalWrite(TURN_LEFT_PIN, GPIO.LOW)
    wiringpi.pinMode(TURN_RIGHT_PIN, GPIO.OUTPUT)
    wiringpi.digitalWrite(TURN_RIGHT_PIN, GPIO.LOW)

    algo = algo_sel.FEATURE
    image_filter = []

    source = cv2.VideoCapture(s)
    X_MIDLINE = int(source.get(cv2.CAP_PROP_FRAME_WIDTH))/2
    print("MID", X_MIDLINE)
    win_name = "Camera Preview"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    fps = FPS().start()

    return (source, win_name, fps, image_filter, algo, X_MIDLINE)
