#########################################
#
# This function accepts the coordinates of the found shapes' corners,
# calculates the target's midpoint based on each measurement, then 
# does a weighted average to determine the final midpoint. Then, it 
# subtracts the midpoint from the midline of the camera, and scales down and returns the result
# 
# Functions:
# computeTurn(hz_bar, vert_bars, X_MIDLINE)
# hz_bar - list of [x_min, x_max, y_coord] for all found lines
# vert_bars - coords of corners of found vertical bars
# X_MIDLINE - 1/2 the max value of x in the camera's output, found in init()
#
# Author: Caden Daffron
#
#########################################
# INDEX CONSTANTS
HZ_X_MIN = 0
HZ_X_MAX = 1
HZ_Y_COORD = 2

LEFT_BAR = 0
RIGHT_BAR = 1
TOP_LEFT = 0
BOTTOM_RIGHT = 1
VERT_X = 0
VERT_Y = 1
# END INDEX CONSTANTS

# CONSTANT PARAMETERS
HZ_MIDPOINT_WT = 0.7
VT_MIDPOINT_WT = 0.3
THROW_READY_TURN_TH = 10
SLOW_TURN_TH = 40   
# END CONSTANT PARAMETERS

def computeTurn(hz_bar, vert_bars, X_MIDLINE):
    count = 0
    hz_midpoint = None
    vert_midpoint = None
    if hz_bar != []:
        hz_midpoint = 0
        for row in hz_bar:
            hz_midpoint += ((row[HZ_X_MAX] - row[HZ_X_MIN]) / 2) + row[HZ_X_MIN]
            count += 1

        hz_midpoint /= count

    if vert_bars[LEFT_BAR] != [] and vert_bars[RIGHT_BAR] != []:
        left_edge = vert_bars[LEFT_BAR][TOP_LEFT][VERT_X]
        right_edge = vert_bars[RIGHT_BAR][BOTTOM_RIGHT][VERT_X]
        vert_midpoint = ((right_edge - left_edge) / 2) + left_edge

    count = 0
    avg_midpoint = 0
    overall_wt = 0
    if hz_midpoint != None:
        avg_midpoint += hz_midpoint
        overall_wt += HZ_MIDPOINT_WT
        count += 1

    if vert_midpoint != None:
        avg_midpoint += vert_midpoint
        overall_wt += VT_MIDPOINT_WT
        count += 1

    if count != 0:
        avg_midpoint /= overall_wt * count
    
    print("Avg_midpoint", avg_midpoint)

    error = (avg_midpoint - X_MIDLINE) / 4
    if abs(error) > 127:
        return 127 * (abs(error)/error)
    elif abs(error) < THROW_READY_TURN_TH:
        return 0
    elif abs(error) < SLOW_TURN_TH:
        return error * 0.5
    else:
        return error
