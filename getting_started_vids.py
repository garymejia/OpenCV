import numpy as np
import cv2 as cv

#argument can be either the device index or the name of the video file
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot open camera")
    exit()

while True:
    #capture frame by frame
    ret, frame = cap.read()

    #if frame is read correctly ret is True
    if not ret:
        print("cant receive frame(end stream?) exiting...")
        break
    #our operations on the fram come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

#when everything is done, release the capture
cap.release()
cv.destroyAllWindows()