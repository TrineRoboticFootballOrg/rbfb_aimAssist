######################################################
# THIS FILE IS DEPRECATED
# This file handles keystrokes, to apply/remove filters, select algorithm, and exit the program
#
# Author: Caden Daffron
#
######################################################

import cv2
from init import algo_sel, filter_mode

def checkKeystroke(image_filter, algo):
    quit_prg = 0
    key = cv2.waitKey(1)
    if key == ord("C") or key == ord("c"):
        algo = algo_sel.CANNY
    elif key == ord("F") or key == ord("f"):
        algo = algo_sel.FEATURE 
    elif key == ord("U") or key == ord("u"):
        algo = algo_sel.CLUSTER
    elif key == ord("B") or key == ord("b"):
        if filter_mode.BLUR in image_filter:
            image_filter.remove(filter_mode.BLUR)
        else:
            image_filter.append(filter_mode.BLUR)
    elif key == ord("I") or key == ord("i"):
        if filter_mode.HSV in image_filter:
            image_filter.remove(filter_mode.HSV)
        else:
            image_filter.append(filter_mode.HSV)
    elif key == 27:
    	quit_prg = 1

    return (image_filter, algo, quit_prg)
