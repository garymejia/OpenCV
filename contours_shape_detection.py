import cv2 as cv
from joining_images import StackedImages as stack
import numpy as np

def getContours(img):
    contours, Hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        #print(area)
        if area > 44:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            #print(peri)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            else if objCor == 4:
            else:
                objectType = "None"
            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(imgContour, objectType,(x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)
path = "shapes.png"
imgOriginal = cv.imread(path)
img = cv.resize(imgOriginal, (0,0), fx=2, fy=2)
imgContour = img.copy()
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50 ,50)
getContours(imgCanny)
images = stack()
imgBlank = np.zeros_like(img)
stackimgs = images.stackImages(0.8, ([img, imgGray, imgBlur],
                                    [imgCanny, imgContour, imgBlank]))

cv.imshow("imgs", stackimgs)
#cv.imshow("original", img)
cv.waitKey(0)