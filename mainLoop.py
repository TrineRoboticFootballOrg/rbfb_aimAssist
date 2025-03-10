import cv2
import sys
import wiringpi
import filterCamFrame as fCF
#import featureTrack as fT
import init
from imutils.video import FPS



def checkKeystroke(image_filter, algo):
    quit_prg = 0
    key = cv2.waitKey(1)
    if key == ord("C") or key == ord("c"):
        algo = algo_sel.CANNY
    elif key == ord("F") or key == ord("f"):
        algo = algo_sel.FEATURE 
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


def mainLoop():
    vision_ON = False
    quit_prg = 0
    source, win_name, fps, image_filter, algo, X_MIDLINE = init.init()

    while 1:
        print("Vision OFF")
        print("PIN READ:", wiringpi.digitalRead(init.VISION_ACT_PIN))
        if wiringpi.digitalRead(init.VISION_ACT_PIN):
            vision_ON = True
            print("Vision TURNING ON")
       
        while vision_ON:
            has_frame, frame = source.read()
            if not has_frame:
                print("Failed to get frame")
                break

            image_filter, algo, quit_prg = checkKeystroke(image_filter, algo)
            
            if quit_prg:
                break

            frame = fCF.filterCamFrame(frame, image_filter)
            frame = fCF.applyAlgo(frame, algo, X_MIDLINE)
            fps.update()
            fps.stop()
            text = "FPS: {:.2f}".format(fps.fps())
            cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            cv2.imshow(win_name, frame)


            if not wiringpi.digitalRead(init.VISION_ACT_PIN):
                print("Vision TURNING OFF")
                vision_ON = False

        if quit_prg:
           break

    source.release()
    cv2.destroyWindow(win_name)
		
		
mainLoop()
