from detectLine import detectLine

# Physical Values
MIN_HZ_LINE_LEN = 75
MAX_HZ_LINE_LEN = 460
DETECT_HZ_BAND_MIN = 1 #TODO:: Find value Experimentally
MIN_HZ_BAR_THICKNESS = 5
MAX_HZ_BAR_THICKNESS = 45
# End Physical Values

def detectHorizontal(frame):

    FRAME_HEIGHT = len(frame)
    hz_found = False
    hz_bar = []
    
    for i in range(DETECT_HZ_BAND_MIN, FRAME_HEIGHT):
        row = frame[i]
        
        temp_bounds = detectLine(row, MIN_HZ_LINE_LEN, MAX_HZ_LINE_LEN)
        
         
        if temp_bounds != [None, None]:
            temp_bounds.append(i) # Append row num
            hz_bar.append(temp_bounds) # [X_MIN, X_MAX, Y_COORD]
            #print("Appended", temp_bounds)
            if len(hz_bar) == MIN_HZ_BAR_THICKNESS:
                hz_found = True
                #print("horizontal bar found")
            elif len(hz_bar) == MAX_HZ_BAR_THICKNESS:
                hz_found = False
                print("False Positive Detected")
                hz_bar = []
        elif hz_found and temp_bounds == [None, None]:
            break

    return hz_bar
