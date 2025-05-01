#########################################
#
# This function accepts a single row from the pre-processed frame and determines
# whether or not there is a continuous line in the row
# 
# Functions:
# detectLine(row)
# row - a single row of values from the frame, each element being either 0 or 255
#
# Author: Caden Daffron
#
#########################################

# Constant Parameters
MAX_GAP = 3
# End Constant Parameters

# Indexes
LEFT_BOUND = 0
RIGHT_BOUND = 1
# End Indexes

#test_row = [0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 255, 255, 255, 0, 0]

def detectLine(row, MIN_LINE_LEN, MAX_LINE_LEN):
    line_start = 0
    line_found = False
    line_unbroken = True
    line_len = 0
    gap = 0
    bounds = [None, None]

    #print(row)

    while 1:

        if not not row[line_start]:
            gap = 0
            line_len = 0
            line_unbroken = True

            #print("start:", line_start)
            
            while line_unbroken and (line_start + line_len + gap) < len(row):
                
                #print("----------Checking space:", line_start + line_len + gap, ":data:", row[line_start + line_len + gap])
                
                if not not row[line_start + line_len + gap]:
                    line_len += 1 + gap
                    gap = 0
                    if line_len == MIN_LINE_LEN:
                        #print("Line found")
                        #print("Left Bound:", line_start)
                        line_found = True
                        bounds[LEFT_BOUND] = line_start
                    elif line_len == MAX_LINE_LEN:
                        line_found = False
                        bounds = [None, None]
                        break

                else:
                    gap += 1


                if gap > MAX_GAP:
                    #print("Line broken")
                    line_unbroken = False
        if (line_start + line_len + gap) >= len(row) - 1 or not line_unbroken:
            break
        line_start += 1
    
    if line_found:
        bounds[RIGHT_BOUND] = line_start + line_len - 1
        #print("Right Bound:", bounds[RIGHT_BOUND])

    return bounds
