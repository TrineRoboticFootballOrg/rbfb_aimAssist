import cv2
import numpy
from init import filter_mode, algo_sel
from findAndTurn import findAndTurn


feature_params = dict(maxCorners=500, qualityLevel=0.8, minDistance=15, blockSize=9)

def filterCamFrame(frame, image_filter):
    result = frame
    if filter_mode.BLUR in image_filter:
        result = cv2.blur(frame, (13, 13))
    elif filter_mode.HSV in image_filter:
        result = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    return result
    

def applyAlgo(frame, algo, X_MIDLINE):

    if algo == algo_sel.FEATURE:
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            x_vals = []
            for x, y in numpy.float32(corners).reshape(-1, 2):
                cv2.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)
                x_vals.append(x)
                findAndTurn(x_vals, X_MIDLINE)

    elif algo == algo_sel.CANNY:
        result = cv2.Canny(frame, 80, 150)
        
    return result
