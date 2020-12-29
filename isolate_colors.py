import cv2 as cv
import numpy as np
from joining_images import StackedImages

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
stack = StackedImages()
def empty():
    pass

cv.namedWindow("HSV")
cv.resizeWindow("HSV", 640, 240)
cv.createTrackbar("Hue Min", "HSV", 38, 179, empty)
cv.createTrackbar("Hue Max", "HSV", 99, 255, empty)
cv.createTrackbar("Sat Min", "HSV", 79, 255, empty)
cv.createTrackbar("Sat Max", "HSV", 179, 179, empty)
cv.createTrackbar("Val Min", "HSV", 170, 255, empty)
cv.createTrackbar("Val Max", "HSV", 255, 255, empty)

while True:
    _, img = cap.read()
    imgBlank = np.zeros_like(img)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "HSV")
    h_max = cv.getTrackbarPos("Hue Max", "HSV")
    s_min = cv.getTrackbarPos("Sat Min", "HSV")
    s_max = cv.getTrackbarPos("Sat Max", "HSV")
    v_min = cv.getTrackbarPos("Val Min", "HSV")
    v_max = cv.getTrackbarPos("Val Max", "HSV")

    print(h_min)

    upper = np.array([h_max, s_max, v_max])
    lower = np.array([h_min, s_min, v_min])
    mask = cv.inRange(imgHSV, lower, upper)
    result = cv.bitwise_and(img, img, mask = mask)
    #imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
    edged_frame = cv.Canny(result, 100, 200)
    

    #mask = cv.inRange(imgHSV, lower, upper)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    final_stack = stack.stackImages(0.8, ([img, mask, result],
                                    [edged_frame, imgBlank, imgBlank]))
    #hstack = np.hstack([img, mask, result, edged_frame])
    cv.imshow('Horizontal Stacking', final_stack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv.destroyAllWindows()
