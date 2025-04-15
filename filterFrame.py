###############################################
#
# This file takes in a still image and applies the selected filters to it.
#
# Author: Caden Daffron
#
###############################################

import cv2

def filterFrame(frame):
    result = frame
    frame_inv = ~frame # Inverse frame colors so we can look for blue later instead of red
    result = cv2.cvtColor(frame_inv, cv2.COLOR_BGR2HSV)
    
    # Apply threshold to filter out anything that isn't bright red (inverted to blue above)
    result = cv2.inRange(result, (90-10, 70, 50), (90+10, 255, 255))
    #print(result)


    return result
    

