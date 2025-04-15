####################################
#
# This file is deprecated
#
####################################

import cv2
import numpy as np
from imutils.video import FPS

OBJECT_TRACKERS = {
        "csrt": cv2.legacy.TrackerCSRT_create,
        "kcf": cv2.TrackerKCF_create,
        "mosse": cv2.legacy.TrackerMOSSE_create
        }


def objTrack(frame, algo, initBB, fps):
    tracker = OBJECT_TRACKERS[algo]()
    tracker.init(frame, initBB)
    #frame = imutils.resize(frame, width=500)   # Can implement if running too slowly
    (H, W) = frame.shape[:2]

    if initBB is not None:

        (success, box) = tracker.update(frame)

        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                    (0, 255, 0), 2)

        fps.update()
        fps.stop()

        info = [
                ("Tracker", algo),
                ("Success", "Yes" if success else "No"),
                ("FPS", "{:.2f}".format(fps.fps())),
                ]

        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
