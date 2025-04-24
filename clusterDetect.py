###################################
#
# This file contains the custom cluster detection algorithm. It takes in the still image after pre-processing, 
# iterates through it one row of pixels at a time, searching for a continuous line of ON pixels which represents the top bar of the receiver.
# In the future, should also look for vertical bars, and take into account the 'aspect ratio' of the bot, post thickness, etc
# It then averages the lengths of each found line to find the midpoint of the receiver, to be passed along for aiming purposes
# It also calls the compute distance function to find the distance for throw power
#
# Functions:
# clusterDetect(frame, X_MIDLINE)
# frame - image after inversion, transform to HSV, and thresholding. 2D matrix of values 0 and 255, size depending on webcam resolution
# X_MIDLINE - constant int, 1/2 of X_MAX 
#
# Author: Caden Daffron
#
###################################

from detectHorizontal import detectHorizontal
from detectVertical import detectVerticals
from computeDist import avgDist
from computeTurn import computeTurn

# Indexes
X_MIN_COORD  = 0
X_MAX_COORD  = 1
ROW_NUM_IND  = 2
# End Indexes

#test_frame = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 255, 255, 255, 255, 0, 0],
#              [0, 0, 255, 255, 255, 255, 255, 255, 0, 0],
#              [0, 255, 255, 255, 255, 255, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def clusterDetect(frame, X_MIDLINE):
   
    # Format: [X_MIN, X_MAX, Y_COORD]
    hz_bar = detectHorizontal(frame)
    
    # If hz_bar is found, only look below it for the vertical bars. Saves computation time by eliminating space above
    detect_vert_band_min = 9999999 # Placeholder, will be overridden
    if hz_bar != []:
        for row in hz_bar:
            if row[X_MIN_COORD] != None and row[X_MIN_COORD] < detect_vert_band_min:
                detect_vert_band_min = row[X_MIN_COORD]
    else:
        detect_vert_band_min = 0
    
    # Format: [Left_Bar_Corners, Right_Bar_Corners]
    # Format: [[[Top_Left_x, Top_Left_y], [Bot_Right_x, Bot_Right_y]], 
    #          [[Top_Left_x, Top_Left_y], [Bot_Right_x, Bot_Right_y]]]
    vert_bars = detectVerticals(frame, detect_vert_band_min)
    
    if hz_bar == [] and vert_bars == [[],[]]:
        print("Shape not found")
        return (frame, None, None)
    
    #print("Hz Bar:", hz_bar)
    #print("Vert Bar:", vert_bars)
    dist = avgDist(hz_bar, vert_bars)
    turn = computeTurn(hz_bar, vert_bars, X_MIDLINE)
    print("Turn:", turn)
    print("Dist_ft:", dist)
    return frame, turn, dist

#clusterDetect(test_frame)
