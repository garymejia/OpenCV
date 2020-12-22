import cv2 as cv
import numpy as np

img = cv.imread("lena.png")
#(size of the matrix, type of object - values can range from 0-255)
kernel = np.ones((5, 5), np.uint8)

#cvtColor function
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#blur function
#second parameter/kernel size has to be an odd number
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 0)
#Canny edge detection
imgCanny = cv.Canny(img, 150, 200)
#
imgDilation = cv.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv.erode(imgDilation, kernel, iterations=1)

cv.imshow("Blur Image", imgBlur)
cv.imshow("Gray Image", imgGray)
cv.imshow("Canny Image", imgCanny)
cv.imshow("Dilation Image", imgDilation)
cv.imshow("Eroded Image", imgEroded)
cv.waitKey(0)