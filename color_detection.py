import cv2 as cv

path = cv.imread("lambo.png")
cv.namedWindow("TrackBars")
cv.resize("TrackBars", 640, 240)
cv.createTrackbar("Hue Min", "TrackBars", 0, 179)

imgHSV = cv.cvtColor(path, cv.COLOR_BGR2HSV)

cv.imshow("original", path)
cv.imshow("img HVS", imgHSV)

cv.waitKey(0)