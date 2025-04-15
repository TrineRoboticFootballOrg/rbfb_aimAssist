#####################################################
#
# This is the main loop of the program, which calls all lower functions
#
# Author: Caden Daffron
#
####################################################
import cv2
import time
#import wiringpi
from gpiozero import Button, LED
import init
from filterFrame import *
from clusterDetect import clusterDetect
from displayFrame import *
from UARTTrans import *
#from imutils.video import FPS
# CONSTANT PARAMETERS
THROW_READY_MIN_FRAMES = 5 # Number of consecutive frames in which turn must be < THROW_READY_TURN_TH to initiate throw
# END CONSTANT PARAMETERS



def mainLoop():
    vision_ON = True
    quit_prg = 0
    source, win_name, Tx_PIN, VISION_ACT_PIN, X_MIDLINE = init.init()
    throw_ready_countdown = THROW_READY_MIN_FRAMES
    while 1:
        if VISION_ACT_PIN.is_pressed:
            vision_ON = True
            throw_ready_countdown = THROW_READY_MIN_FRAMES
       
        while vision_ON:
            start_time = time.time()
            has_frame, frame = source.read()
            if not has_frame:
                print("Failed to get frame")
                break
            
            #if cv2.waitKey(1) == 27: # Exit if escape key pressed
            #    break

            frame = filterFrame(frame)
            cd_start = time.time()
            frame, turn, dist = clusterDetect(frame, X_MIDLINE)
            cd_end = time.time()
            print("Cluster Detect time:", cd_end-cd_start)
            #print("Past turns:", past_turns)
            if turn != None and turn == 0:
                throw_ready_countdown -= 1
                if throw_ready_countdown == 0:
                    print("SENDING THROW READY ------------------------------")
                    UARTTrans(THROW_MSG, 0, Tx_PIN)
            else:
                throw_ready_countdown = THROW_READY_MIN_FRAMES

            if dist != None:
                pass
                UARTTrans(DIST_MSG, dist, Tx_PIN)
                print("Sending DIST:", DIST_MSG, dist)
            if turn != None:
                UARTTrans(TURN_MSG, turn, Tx_PIN)
                print("Sending TURN:", TURN_MSG, turn)



            if not VISION_ACT_PIN.is_pressed:
                print("Vision TURNING OFF")
                vision_ON = False

            end_time = time.time()
            #print("Mainloop time:", end_time - start_time)
            displayFrame(frame, win_name, vision_ON, end_time - start_time)
        
        #if cv2.waitKey(1) == 27: # Exit if escape key pressed
        #    break
        


    source.release()
    cv2.destroyWindow(win_name)
		
		
mainLoop()
