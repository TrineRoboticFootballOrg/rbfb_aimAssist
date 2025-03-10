##############################
#
# This is a script to take in a list of x values, average them to find
# the approximate midpoint of the object being tracked, and determine
# the direction to turn.
# 
# Written by: Caden Daffron
##############################
import wiringpi
from wiringpi import GPIO
import init

def findAndTurn(x_vals, X_MIDLINE):
    total = 0
    turn = 0 # Turn direction: -1=left, 0=none, 1=right
    
    for x in x_vals:
        total += x
    pos = total/len(x_vals)
    #print("POS", pos)
    if pos > X_MIDLINE:
        turn = -1
        wiringpi.digitalWrite(init.TURN_LEFT_PIN, GPIO.LOW)
        wiringpi.digitalWrite(init.TURN_RIGHT_PIN, GPIO.HIGH)
    elif pos < X_MIDLINE:
        turn = 1
        wiringpi.digitalWrite(init.TURN_RIGHT_PIN, GPIO.LOW)
        wiringpi.digitalWrite(init.TURN_LEFT_PIN, GPIO.HIGH)
    else: 
        turn = 0
        wiringpi.digitalWrite(init.TURN_RIGHT_PIN, GPIO.LOW)
        wiringpi.digitalWrite(init.TURN_LEFT_PIN, GPIO.LOW)

    return turn
