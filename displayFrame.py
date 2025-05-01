#########################################
#
# This function displays various debug information on the cv2 preview of the frame
# 
# Functions:
# displayFrame(frame, win_name, enable, delta_time)
# frame - the pre-processed camera frame, each element being either 0 or 255
# win_name - the name of the cv2 window housing the preview
# enable - bool Is aimAssist enabled
# delta_time - the period of mainLoop
#
# Author: Caden Daffron
#
#########################################
import cv2
import init

def displayFrame(frame, win_name, enable, delta_time):


    #print("Vision Enable:", enable)
    #print("PIN READ:", wiringpi.digitalRead(init.VISION_ACT_PIN))

    #text = ["Test"]

    #for i in range(len(text)):
        #cv2.putText(frame, text[i], (10, (20 + (i*20))), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
   

    print("Mainlooooooooooooooooop time:{:.4f}".format(delta_time))

    #cv2.imshow(win_name, frame)
