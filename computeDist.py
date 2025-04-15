#########################################
#
# This function takes input of the length(in pixels)
# of the top bar and calculates the receiver's distance using the pinhole projection formula
# 
# Author: Caden Daffron
#
#########################################


# PHYSICAL VALUES
CAM_FOCAL_LEN_MM = 4.0
CAM_PX_WID_MM = 4.396
HZ_BAR_LEN_MM = 342.9
HZ_BAR_THK_MM = 22.2
VERT_BAR_LEN_MM = 260.35
VERT_BAR_THK_MM = 22.2
# END PHYSICAL VALUES

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
DIST_BY_HZ_LEN_WT = 0.7
DIST_BY_HZ_THK_WT = 0.2
DIST_BY_VT_LEN_WT = 0.05
DIST_BY_VT_THK_WT = 0.05
# END CONSTANT PARAMETERS


def avgDist(hz_bar, vert_bars):
    count = 0
    avg_hz_len = 0
    
    if hz_bar != []:
        # Average the x-dimension length of each row in hz_bar
        for row in hz_bar:
            avg_hz_len += row[HZ_X_MAX] - row[HZ_X_MIN]
            count += 1
        avg_hz_len /= count

        dist_by_hz_len = computeDist(avg_hz_len, HZ_BAR_LEN_MM)

        # Find thickness of hz_bar by subtracting row num (y-coord) min from max
        avg_hz_thk = 1 + hz_bar[-1][HZ_Y_COORD] - hz_bar[0][HZ_Y_COORD]
        # If hz_bar is only one row, avg_hz_thickness will be 0 and cause a div by 0 error
        if not avg_hz_thk:
            dist_by_hz_thk = computeDist(avg_hz_thk, HZ_BAR_THK_MM)
        else:
            dist_by_hz_thk = None
    else:
        dist_by_hz_len = None
        dist_by_hz_thk = None

    count = 0
    avg_vert_bar_thk = 0
    avg_vert_bar_len = 0
    dist_by_vert_thk = None
    dist_by_vert_len = None
    
    if vert_bars[LEFT_BAR] != []:
        avg_vert_bar_thk += vert_bars[LEFT_BAR][BOTTOM_RIGHT][VERT_X] - vert_bars[LEFT_BAR][TOP_LEFT][VERT_X]
        avg_vert_bar_len += vert_bars[LEFT_BAR][BOTTOM_RIGHT][VERT_Y] - vert_bars[LEFT_BAR][TOP_LEFT][VERT_Y]
        count += 1
        
        if vert_bars[RIGHT_BAR] != []:
            avg_vert_bar_thk += vert_bars[RIGHT_BAR][BOTTOM_RIGHT][VERT_X] - vert_bars[RIGHT_BAR][TOP_LEFT][VERT_X]
            avg_vert_bar_len += vert_bars[RIGHT_BAR][BOTTOM_RIGHT][VERT_Y] - vert_bars[RIGHT_BAR][TOP_LEFT][VERT_Y]
            count += 1
    
        avg_vert_bar_thk /= count
        avg_vert_bar_len /= count
        dist_by_vert_thk = computeDist(avg_vert_bar_thk, VERT_BAR_THK_MM)
        dist_by_vert_len = computeDist(avg_vert_bar_len, VERT_BAR_LEN_MM)
   
    overall_avg_dist = 0
    wt_sum = 0

    if dist_by_hz_len != None:
        overall_avg_dist += dist_by_hz_len * DIST_BY_HZ_LEN_WT
        wt_sum += DIST_BY_HZ_LEN_WT

    if dist_by_hz_thk != None:
        overall_avg_dist += dist_by_hz_thk * DIST_BY_HZ_THK_WT
        wt_sum += DIST_BY_HZ_THK_WT

    if dist_by_vert_thk != None:
        overall_avg_dist += dist_by_vert_thk * DIST_BY_VT_THK_WT
        wt_sum += DIST_BY_VT_THK_WT

    if dist_by_vert_len != None:
        overall_avg_dist += dist_by_vert_len * DIST_BY_VT_LEN_WT
        wt_sum += DIST_BY_VT_LEN_WT

    overall_avg_dist /= wt_sum
    print("Hz len:", avg_hz_len)
    print("Hz len dist:", dist_by_hz_len)
    print("Hz thk:", avg_hz_thk)
    print("Hz thk dist:", dist_by_hz_thk)
    print("Vt len:", avg_vert_bar_len)
    print("Vt len dist:", dist_by_vert_len)
    print("Vt thk:", avg_vert_bar_thk)
    print("Vt thk dist:", dist_by_vert_thk)
    print("dist:", overall_avg_dist)
    return round(overall_avg_dist + 0.5)


def computeDist(pixel_dim, MM_DIM):

    dist_m = (MM_DIM * CAM_FOCAL_LEN_MM) / (CAM_PX_WID_MM * pixel_dim)
    dist_ft = dist_m * 3.28084
    return dist_ft
