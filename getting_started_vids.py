import numpy as np
import cv2 as cv

#argument can be either the device index or the name of the video file
cap = cv.VideoCapture(0)

#define the codec and create a VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
"""
access some of caps features with cap.get(propId)
propId -> 0-18 and denotes a property from the video

in contrast some of these properties can be modified using .set(propId, value)
"""


while cap.isOpened():
    #capture frame by frame
    #cap.read() returns true if frame is read correctly
    ret, frame = cap.read()

    #if frame is read correctly ret is True
    if not ret:
        print("cant receive frame(end stream?) exiting...")
        break
    
    
    frame = cv.flip(frame, 0)
    #write the flipped frame
    out.write(frame)


    #display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

#when everything is done, release everything
cap.release()
out.release()
cv.destroyAllWindows()