
from detectHorizontal import detectLine

# Physical Parameters
MIN_VERT_BAR_TH = 2
MAX_VERT_BAR_TH = 45
MIN_GAP_FOR_VT = 70 
MAX_GAP_FOR_VT = 375
MIN_VERT_LINE_LEN = 35
MAX_VERT_LINE_LEN = 340
# End Physical Parameters

# Index Constants
LEFT_BAR = 0
RIGHT_BAR = 1

TOP_LEFT = 0
TOP_RIGHT = 1

X_COORD = 2
Y_MIN_COORD = 0
Y_MAX_COORD = 1
#End Index Constants

test_frame = [[0,   0,   0,   0, 255, 255, 255,   0, 0, 0],
              [0,   0,   0, 255, 255, 255, 255, 255, 0, 0],
              [0,   0, 255, 255, 255,   0, 255, 255, 0, 0],
              [0, 255, 255, 255, 255,   0, 255, 255, 0, 0],
              [0,   0,   0,   0,   0,   0,   0,   0, 0, 0]]

def detectVerticals(frame, detect_vert_band_min):
    # Format: [Left_Bar_Corners, Right_Bar_Corners]
    # Format: [[[Top_Left_x, Top_Left_y], [Bot_Right_x, Bot_Right_y]], [[Top_Left_x, Top_Left_y], [Bot_Right_x, Bot_Right_y]]]
    col_corners = [[], []] 
    vert_bars = [[], []]
    lr_bar = LEFT_BAR
    vert_found = [False, False]
    for i in range(detect_vert_band_min, len(frame[0])):

        col = [] 
        for row in frame:
            col.append(row[i])
            
        temp_bounds = detectLine(col, MIN_VERT_LINE_LEN, MAX_VERT_LINE_LEN)
            
        if temp_bounds != [None, None]:
            temp_bounds.append(i)
            vert_bars[lr_bar].append(temp_bounds)

            if len(vert_bars[lr_bar]) == MIN_VERT_BAR_TH:
                if vert_found[LEFT_BAR]  == False:    
                    vert_found[LEFT_BAR] = True
                    #print("Left vert bar found")
                else:
                    vert_found[RIGHT_BAR] = True
                    #print("Right vert bar found")

        elif vert_found == [True, True] and temp_bounds == [None, None]:
            break
        elif vert_found[LEFT_BAR] == True and temp_bounds == [None, None]:
            lr_bar = RIGHT_BAR
            #print("Left bar ended")
    #print(vert_bars)
    if vert_found[LEFT_BAR]:
        col_corners[LEFT_BAR].append([vert_bars[LEFT_BAR][0][X_COORD], vert_bars[LEFT_BAR][0][Y_MIN_COORD]]) 
        col_corners[LEFT_BAR].append([vert_bars[LEFT_BAR][-1][X_COORD], vert_bars[LEFT_BAR][-1][Y_MAX_COORD]])
    
    if vert_bars[RIGHT_BAR] != []:
        col_corners[RIGHT_BAR].append([vert_bars[RIGHT_BAR][0][X_COORD], vert_bars[RIGHT_BAR][0][Y_MIN_COORD]])
        col_corners[RIGHT_BAR].append([vert_bars[RIGHT_BAR][-1][X_COORD], vert_bars[RIGHT_BAR][-1][Y_MAX_COORD]])
    
    #print(col_corners)
    
    return col_corners

#detectVertical(test_frame, 0)
