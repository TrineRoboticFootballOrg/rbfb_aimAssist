##############################
#
# This is file takes in a list of x values, averages them to find
# the approximate midpoint of the object being tracked, and determine
# the direction to turn.
# 
# Author: Caden Daffron
##############################

# TODO::Update this to generate 8-bit ints based on turn speed

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
    elif pos < X_MIDLINE:
        turn = 1
    else: 
        turn = 0

    return turn
