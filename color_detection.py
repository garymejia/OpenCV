import cv2 as cv
import numpy as np
from joining_images import StackedImages

def empty(a):
    pass

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)
cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 98, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 121, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
joinedIMg = StackedImages()

while True:
    path = cv.imread("lambo.png")
    imgHSV = cv.cvtColor(path, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(path, lower, upper)
    imgResult = cv.bitwise_and(path, path, mask=mask)

    """cv.imshow("original", path)
    cv.imshow("mask", mask)
    cv.imshow("img Result", imgResult)
    """
    imgStack = joinedIMg.stackImages(0.6, ([path,path],[mask, imgResult]))
    cv.imshow("stack", imgStack)
    cv.waitKey(1)