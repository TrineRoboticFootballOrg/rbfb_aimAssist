############################################
#
# This file takes in the frame, routes it to the selected algorithm,
# and passes the returned midpoint to the findAndTurn function
#
# Author: Caden Daffron
#
###########################################

import cv2
import time
import numpy
from init import algo_sel
from findAndTurn import findAndTurn
import clusterDetect as cD

feature_params = dict(maxCorners=500, qualityLevel=0.8, minDistance=15, blockSize=9)

#TODO:: Don't actually need to pass in X_MIDLINE, can determine from frame
def applyAlgo(frame, algo, X_MIDLINE):

    if algo == algo_sel.FEATURE:
        result = frame
        #corners = cv2.goodFeaturesToTrack(frame, **feature_params)
        #if corners is not None:
        #    x_vals = []
        #    for x, y in numpy.float32(corners).reshape(-1, 2):
        #        cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)
        #        x_vals.append(x)
        #        findAndTurn(x_vals, X_MIDLINE)

    elif algo == algo_sel.CANNY:
        result = cv2.Canny(frame, 80, 150)
    
    elif algo == algo_sel.CLUSTER:
        start_time = time.time()
        corners = cD.clusterDetect(frame)
        end_time = time.time()
        print("Cluster Detection Time={:.4f}".format(end_time-start_time))
        #print("Corners:", corners)
        if corners != []:
            result = frame#cv2.rectangle(frame, corners[0], (corners[1][0], corners[1][1]), (0, 0, 255), 2)
        else:
            result = frame

    return result
