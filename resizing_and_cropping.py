import cv2 as cv
import numpy as np


img = cv.imread("lambo.png")
#print(img.shape)
#Resized Image
"""
Remove whitespace
imgResize = cv.resize(img, (300, 200))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = 255*(gray < 128).astype(np.uint8)
"""
#Crop image, height first and then width
imgCropped = img[0:200, 200:500]


cv.imshow("Image", img)
#cv.imshow("Image Resize", imgResize)
#cv.imshow("Image Cropped", imgCropped)

cv.waitKey(0)