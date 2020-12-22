import cv2 as cv
import numpy as np

img = cv.imread("cards.jpeg")
width,height = 250, 350
pts1 = np.float32([[71, 222],[164, 202],[50, 104],[134, 86]])
pts2 = np.float32([[0,0],[width, 0],[0, height],[width, height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))
cv.imshow("Image", img)
cv.imshow("output image", imgOutput)
cv.waitKey(0)